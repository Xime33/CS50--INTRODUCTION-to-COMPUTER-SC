// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open input file
    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Could not open input file.\n");
        return 1;
    }

    // Open output file
    FILE *output = fopen(argv[2], "wb");
    if (output == NULL)
    {
        fclose(input);
        printf("Could not open output file.\n");
        return 1;
    }

    // Convert factor from string to float
    float factor = atof(argv[3]);

    // Allocate memory for the header
    uint8_t header[HEADER_SIZE];

    // Read header from input file
    if (fread(header, sizeof(uint8_t), HEADER_SIZE, input) != HEADER_SIZE)
    {
        fclose(input);
        fclose(output);
        printf("Error reading header from input file.\n");
        return 1;
    }

    // Write header to output file
    if (fwrite(header, sizeof(uint8_t), HEADER_SIZE, output) != HEADER_SIZE)
    {
        fclose(input);
        fclose(output);
        printf("Error writing header to output file.\n");
        return 1;
    }

    // Process audio samples
    int16_t sample;
    while (fread(&sample, sizeof(int16_t), 1, input) == 1)
    {
        // Scale the sample
        sample = (int16_t)(sample * factor);

        // Write scaled sample to output file
        if (fwrite(&sample, sizeof(int16_t), 1, output) != 1)
        {
            fclose(input);
            fclose(output);
            printf("Error writing sample to output file.\n");
            return 1;
        }
    }

    // Close files
    fclose(input);
    fclose(output);

    return 0;
}