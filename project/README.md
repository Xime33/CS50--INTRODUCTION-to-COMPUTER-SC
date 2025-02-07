# Discover Your Inner Wizard: Which Harry Potter Character Are You?

#### Video Demo:  <https://youtu.be/dtmGXQWNfJc>

---

## Introduction

Welcome to the **Harry Potter Character Quiz**! This project is an interactive, web-based quiz that transports users into the magical world of Harry Potter. By answering a series of fun, lighthearted, and often humorous questions, users can discover which iconic character from the Harry Potter universe they resemble the most.

Whether you're a brave Gryffindor, an ambitious Slytherin, a wise Ravenclaw, or a kind Hufflepuff, this quiz offers an engaging experience for fans of the wizarding world. With carefully crafted questions, responsive design, and magical aesthetics, this project seeks to bring a smile to every Potterhead who participates.

---

## Files and Their Purpose

### 1. **quiz.html**
This is the core HTML file of the project, responsible for structuring the quiz interface. It includes:
- The **title** of the quiz, displayed prominently at the top.
- A series of **multiple-choice questions**, each styled for clarity and ease of interaction.
- A **result section**, dynamically updated based on user input.

### 2. **styles.css** (Embedded in `quiz.html`)
Custom CSS is embedded within the HTML file for simplicity. It styles the quiz with:
- A **dark magical theme** with gradients and shadows inspired by the Harry Potter universe.
- **Animations** for elements such as the title and result display, enhancing user engagement.
- A **responsive design** that ensures usability across devices, including desktops, tablets, and smartphones.

### 3. **script.js** (Embedded in `quiz.html`)
The JavaScript code handles the logic of the quiz, including:
- **Validating user input**, ensuring all questions are answered before submitting.
- Dynamically hiding questions and displaying results after submission.
- Resetting the quiz for replayability.
- Fetching random results from a backend endpoint to keep the experience fresh.

### 4. **backend.py**
This Python file serves as the backend logic for the project. It:
- Implements an API endpoint (`/random-character`) that randomly selects a Harry Potter character and returns their name and image URL.
- Ensures the quiz is dynamic, making each playthrough unique.

---

## Design Choices and Rationale

### **1. Interactive and Fun**
The primary goal was to create a lighthearted quiz that captures the whimsical spirit of the Harry Potter series. This is reflected in the humorous and engaging question options, like choosing your ideal magical pet or handling funny scenarios at Hogwarts.

### **2. Responsive Design**
The decision to make the layout responsive ensures that the quiz is accessible and visually appealing across all devices. The use of percentage-based widths and flexible font sizes enhances usability, especially for mobile users.

### **3. Simplicity vs. Complexity**
Initially, I debated whether to include more complex logic, such as calculating results based on a scoring system. However, I opted for a simpler random character selection to keep the experience fun and replayable. This decision allowed me to focus on design and usability while maintaining a lightweight backend.

### **4. Embedded Styles and Scripts**
Instead of separating CSS and JavaScript into their own files, I embedded them within the HTML file for simplicity and ease of deployment. This was a deliberate choice to make the project self-contained and straightforward to run on any server.

---

## Features

### **1. Dynamic Question Set**
The quiz includes a series of entertaining questions, covering:
- Magical preferences (e.g., favorite spells or pets).
- Personality traits and reactions to whimsical scenarios.
- Hogwarts-themed choices that feel authentic to the Harry Potter universe.

### **2. Randomized Results**
To keep the quiz engaging, the result is randomized using a backend API. Each playthrough offers the chance to discover a new character, encouraging users to replay and share with friends.

### **3. Engaging Visual Design**
The quiz is styled to reflect the enchanting aesthetic of the wizarding world, with:
- Custom fonts reminiscent of the Harry Potter logo.
- Bold, vibrant colors like Gryffindor gold and Slytherin green.
- Subtle animations for a touch of magic.

### **4. Replayability**
Users can easily reset the quiz and try again, making it perfect for casual fun or group play.

---

## Technologies Used

### **Frontend:**
- **HTML**: Provides the structure for the quiz interface.
- **CSS**: Styles the quiz to align with the magical theme while maintaining responsiveness.
- **JavaScript**: Handles form validation, dynamic content updates, and interactive elements.

### **Backend:**
- **Python**: Implements the logic for generating randomized quiz results.
- **Flask**: Provides the lightweight framework for the backend API.

---

## Challenges and Learnings

### **Challenges:**
1. **Responsive Design:** Ensuring the quiz looked good across various screen sizes required testing and adjustments, particularly for images and font sizes.
2. **Result Randomization:** Balancing simplicity and user engagement meant opting for random results instead of a scoring system.

### **Learnings:**
- Embedding animations and custom fonts can significantly enhance the user experience.
- Testing on different devices is critical for creating a truly responsive design.
- A simple and fun user experience often trumps complexity in lighthearted projects.

---


