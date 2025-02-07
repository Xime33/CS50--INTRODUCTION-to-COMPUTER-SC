-- Keep a log of any SQL queries you execute as you solve the mystery.

-- i use this query to find the id  and the description of the crime
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
-- took place at 10:15 am, at a bakery
 SELECT * FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND DAY = 28 AND hour = 10 AND minute BETWEEN 14 AND 16;
-- id: 259 ENTRANCE, ID: 260 EXIT
--LICENSE_PLATE exit between 10:16am and 10:35am

--5P2BI95
--94KL13X
--6P58WS2
--4328GD8
--G412CB7
--L93JTIZ
--322W7JE
--ONTHK55
--1106N58

-- I USE THIS QUERY TO GET ACCES TO THE INTERVIEWS
SELECT * FROM interviews WHERE year = 2023 AND month = 7 AND DAY = 28;

--to know who made the call
SELECT *
FROM people
WHERE license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', 'ONTHK55', '1106N58');

SELECT phone_calls.*, people.name FROM phone_calls
JOIN people on phone_calls.caller = people.phone_number
WHERE caller = (SELECT phone_number FROM people WHERE name = 'Bruce') and day = 28;

--+-----+----------------+----------------+------+-------+-----+----------+-------+
--| id  |     caller     |    receiver    | year | month | day | duration | name  |
--+-----+----------------+----------------+------+-------+-----+----------+-------+
--| 233 | (367) 555-5533 | (375) 555-8161 | 2023 | 7     | 28  | 45       | Bruce |
--| 236 | (367) 555-5533 | (344) 555-9601 | 2023 | 7     | 28  | 120      | Bruce |
--| 245 | (367) 555-5533 | (022) 555-4052 | 2023 | 7     | 28  | 241      | Bruce |
--| 285 | (367) 555-5533 | (704) 555-5790 | 2023 | 7     | 28  | 75       | Bruce |
--+-----+----------------+----------------+------+-------+-----+----------+-------+

SELECT name FROM people WHERE phone_number = '(375) 555-8161';


SELECT bank_accounts.person_id, people.name, atm_transactions.* FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON bank_accounts.person_id = people.id
 WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street';

--+-----------+------+-----+----------------+------+-------+-----+----------------+------------------+--------+
--| person_id | name | id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
--+-----------+------+-----+----------------+------+-------+-----+----------------+------------------+--------+
--| 467400    | Luca | 246 | 28500762       | 2023 | 7     | 28  | Leggett Street | withdraw         | 48     |
--+-----------+------+-----+----------------+------+-------+-----+----------------+------------------+--------+

SELECT * FROM passengers
JOIN people ON passengers.passport_number = people.passport_number
WHERE people.name = 'Bruce';

--+-----------+-----------------+------+--------+-------+----------------+-----------------+---------------+
--| flight_id | passport_number | seat |   id   | name  |  phone_number  | passport_number | license_plate |
--+-----------+-----------------+------+--------+-------+----------------+-----------------+---------------+
--| 36        | 5773159633      | 4A   | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
--+-----------+-----------------+------+--------+-------+----------------+-----------------+---------------+

SELECT *
FROM flights
JOIN airports AS origin_airport ON flights.origin_airport_id = origin_airport.id
JOIN airports AS destination_airport ON flights.destination_airport_id = destination_airport.id
WHERE flights.id = 36;

