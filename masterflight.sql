-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2023 at 05:08 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `masterflight`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline`
--

CREATE TABLE `airline` (
  `airline_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airline`
--

INSERT INTO `airline` (`airline_name`) VALUES
('Jet Blue'),
('United Airlines');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff`
--

CREATE TABLE `airline_staff` (
  `username` varchar(15) NOT NULL,
  `airline_name` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `first_name` varchar(10) DEFAULT NULL,
  `last_name` varchar(10) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airline_staff`
--

INSERT INTO `airline_staff` (`username`, `airline_name`, `password`, `first_name`, `last_name`, `date_of_birth`) VALUES
('a', 'Jet Blue', '0cc175b9c0f1b6a831c3', 'a', 'a', '2023-05-03'),
('l', 'Jet Blue', '2db95e8e1a9267b7a118', 'LOL', 'l', '2023-05-04'),
('p', 'Jet Blue', '83878c91171338902e0fe0fb97a8c4', 'p', 'p', '2023-04-21'),
('s', 'Jet Blue', 's', 's', 's', '2023-04-26'),
('t', 'United Airlines', 't', 't', 't', '2023-04-27'),
('y', 'Jet Blue', '415290769594460e2e48', 'y', 'y', '2023-05-01'),
('yoyoyo', 'United Airlines', '7b8b965ad4bca0e41ab5', 'jack', 'daniel', '2027-12-18'),
('z', 'United Airlines', 'fbade9e36a3f36d3d676', 'z', 'z', '2023-05-04');

-- --------------------------------------------------------

--
-- Table structure for table `airplane`
--

CREATE TABLE `airplane` (
  `airplane_id` varchar(20) NOT NULL,
  `num_seats` decimal(3,0) DEFAULT NULL,
  `Manufacturing_comp` varchar(20) DEFAULT NULL,
  `Manufacturing_date` date DEFAULT NULL,
  `airline_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airplane`
--

INSERT INTO `airplane` (`airplane_id`, `num_seats`, `Manufacturing_comp`, `Manufacturing_date`, `airline_name`) VALUES
('5FSKHzdy', '121', 'Boeing', '2023-05-01', 'Jet Blue'),
('5lX34iNo', '121', 'Boeing', '2023-05-01', 'Jet Blue'),
('6wZJJmlv', '112', 'Boeing', '2023-05-03', 'Jet Blue'),
('bXWtc5qE', '222', 'Boeing', '2023-05-01', 'Jet Blue'),
('FNnBu3UJ', '80', 'Boeing', '2023-04-01', 'Jet Blue'),
('JA8089', '100', 'Airbus', '2010-05-06', 'Jet Blue'),
('qXfaQ3Xy', '85', 'Airbus', '1995-06-07', 'Jet Blue'),
('RuM2iRQD', '180', 'Boeing', '2023-02-02', 'Jet Blue'),
('rxD79Fk9', '300', 'Boeing', '2023-05-03', 'Jet Blue'),
('S21232', '60', 'Boeing', '2005-05-01', 'Jet Blue'),
('S83943', '90', 'Boeing', '2009-01-06', 'Jet Blue'),
('UA9812', '120', 'Boeing', '2015-02-03', 'United Airlines'),
('W7uEaZRj', '80', 'Boeing', '2023-04-01', 'Jet Blue'),
('YlpZIMrg', '90', 'Boeing', '2023-05-02', 'Jet Blue'),
('zh3UROV7', '180', 'Boeing', '2023-02-02', 'Jet Blue');

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `code` varchar(20) NOT NULL,
  `airport_name` varchar(100) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  `airport_type` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`code`, `airport_name`, `city`, `country`, `airport_type`) VALUES
('ATL', 'Atlanta Airport', 'Atlanta', 'U.S.A.', 'International'),
('CDG', 'Charles de Gaulle', 'Paris', 'France', 'Inter/Dom'),
('JFK', 'John F. Kennedy', 'NYC', 'U.S.A.', 'International'),
('LHR', 'Heathrow', 'London', 'England', 'International'),
('ORD', 'Chicago Airport', 'Chicago', 'U.S.A', 'International'),
('PVG', 'Shanghai Airport', 'Shanghai', 'China', 'International');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `e_mail` varchar(30) NOT NULL,
  `first_name` varchar(10) DEFAULT NULL,
  `last_name` varchar(15) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  `building_num` int(11) DEFAULT NULL,
  `street_name` varchar(20) DEFAULT NULL,
  `apt_num` int(11) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`e_mail`, `first_name`, `last_name`, `password`, `building_num`, `street_name`, `apt_num`, `city`, `state`, `zip_code`) VALUES
('b', 'b', 'b', '92eb5ffee6ae2fec3ad7', 12, 'Jay', 32, 'b', 'n', '12'),
('f', 'f', 'f', '8fa14cdd754f91cc6554', 23, 'f', 2, 'f', 'f', '2'),
('fa', 'fa', 'fa', '89e6d2b383471fc370d8', 3, 'j', 5, 'New York', 'NY', '11111'),
('g', 'g', 'g', '9a0fe27c8bcc9aad51ed', 2, 'g', 2, 'g', 'g', 'g'),
('m', 'm', 'm', '6f8f57715090da263245', 2, 'm', 3, 'm', 'm', '2'),
('n', 'n', 'n', '7b8b965ad4bca0e41ab5', 3, 'n', 2, 'n', 'n', 'n'),
('t', 't', 't', 'e358efa489f58062f10d', 2, 't', 5, 't', 't', 't'),
('u', 'u', 'u', '7b774effe4a349c6dd82', 2, 'u', 2, '2', 'u', 'u'),
('w', 'w', 'w', 'f1290186a5d0b1ceab27', 3, 'jay', 2, 'New York', 'NY', '12121');

-- --------------------------------------------------------

--
-- Table structure for table `customer_phone_num`
--

CREATE TABLE `customer_phone_num` (
  `phone_num` varchar(15) NOT NULL,
  `e_mail` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `flight_num` int(11) NOT NULL,
  `base_price` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `departure_time` time DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  `arrival_time` time DEFAULT NULL,
  `arrival_date` date DEFAULT NULL,
  `departure_airport` varchar(20) DEFAULT NULL,
  `airplane_id` varchar(20) DEFAULT NULL,
  `airline_name` varchar(20) NOT NULL,
  `arrival_airport` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`flight_num`, `base_price`, `status`, `departure_time`, `departure_date`, `arrival_time`, `arrival_date`, `departure_airport`, `airplane_id`, `airline_name`, `arrival_airport`) VALUES
(22, 500000, 'On-time', '15:54:00', '2023-05-16', '18:54:00', '2023-05-16', 'LGA', 'FNnBu3UJ', 'Jet Blue', 'ORD'),
(355, 200, 'Delayed', '16:35:00', '2023-04-05', '17:35:00', '2023-04-05', 'LAX', 'qXfaQ3Xy', 'Jet Blue', 'JFK'),
(378, 125, 'On-time', '19:14:00', '2023-05-04', '20:14:00', '2023-05-04', 'JFK', 'JA8089', 'Jet Blue', 'LGA'),
(425, 120, 'On-time', '03:40:00', '2026-03-11', '08:40:00', '2026-03-11', 'ORD', 'FNnBu3UJ', 'Jet Blue', 'JFK'),
(488, 120, 'Delayed', '11:15:00', '2023-05-05', '15:20:00', '2023-05-05', 'JFK', 'UA9812', 'United Airlines', 'ORD'),
(555, 120, 'On-time', '02:30:00', '2024-03-05', '05:00:00', '2024-03-05', 'JFK', 'S83943', 'Jet Blue', 'ORD'),
(622, 122, 'On-time', '21:27:00', '2023-05-06', '01:27:00', '2023-05-06', 'JFK', 'JA8089', 'Jet Blue', 'LAX'),
(7463, 150, 'Delayed', '01:45:00', '2023-02-01', '05:00:00', '2023-04-06', 'ATL', 'UA9812', 'United Airlines', 'JFK'),
(8989, 200, 'On-time', '15:00:00', '2023-05-10', '09:00:00', '2023-05-10', 'ATL', 'S83943', 'Jet Blue', 'JFK'),
(46574, 130, 'On-time', '04:35:00', '2024-06-05', '05:40:00', '2024-06-05', 'JFK', 'UA9812', 'United Airlines', 'ORD');

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `e_mail` varchar(30) NOT NULL,
  `ticket_id` varchar(20) NOT NULL,
  `purchase_time` time DEFAULT NULL,
  `purchase_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `purchase`
--

INSERT INTO `purchase` (`e_mail`, `ticket_id`, `purchase_time`, `purchase_date`) VALUES
('b', 'CtsHXCzd', '20:26:09', '2023-05-05'),
('b', 'hdsNPPfw', '20:06:11', '2023-05-05'),
('m', '26Xv42l8', '18:06:25', '2023-05-04'),
('m', 'Bf06hkmm', '18:07:26', '2023-05-04'),
('t', 'dBPkU2wV', '16:47:38', '2023-05-04'),
('t', 'ElQaw1cp', '18:18:55', '2023-05-05'),
('t', 'ttt', '05:00:00', '2023-02-05'),
('t', 'z0JtgTFG', '22:06:05', '2023-05-02');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `e_mail` varchar(30) NOT NULL,
  `flight_num` int(11) NOT NULL,
  `rate` decimal(2,1) DEFAULT NULL,
  `comments` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`e_mail`, `flight_num`, `rate`, `comments`) VALUES
('f', 7463, '2.0', 'ieryir'),
('g', 7463, '3.0', 'sdfsaf'),
('t', 7463, '1.0', 'uguguu'),
('t', 46574, '5.0', 'jdksjdsk');

-- --------------------------------------------------------

--
-- Table structure for table `staff_emails`
--

CREATE TABLE `staff_emails` (
  `username` varchar(10) NOT NULL,
  `e_mail` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `staff_phone_numbers`
--

CREATE TABLE `staff_phone_numbers` (
  `username` varchar(10) NOT NULL,
  `phone_num` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `ticket_id` varchar(20) NOT NULL,
  `flight_num` int(11) DEFAULT NULL,
  `ticket_price` int(11) DEFAULT NULL,
  `card_type` varchar(6) DEFAULT NULL,
  `name_on_card` varchar(30) DEFAULT NULL,
  `expiration_date` date DEFAULT NULL,
  `card_num` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`ticket_id`, `flight_num`, `ticket_price`, `card_type`, `name_on_card`, `expiration_date`, `card_num`) VALUES
('26Xv42l8', 555, 132, 'Credit', 'max', '2026-11-04', '121212121221'),
('Bf06hkmm', 8989, 220, 'Credit', 'max', '2026-11-04', '121212121221'),
('bIwlNmSC', 46574, 143, 'Credit', 'george', '2023-05-02', '82738263827383'),
('BN3ujDqY', 555, 132, 'Credit', 'george', '2027-12-02', '82738263827383'),
('CtsHXCzd', 555, 132, 'Credit', 'looooooooooooo', '2023-05-05', '3343443434343'),
('dBPkU2wV', 355, 220, 'Credit', 'george', '2027-12-04', '82738263827383'),
('Ejug1f2U', 555, 132, 'Credit', 'george', '2023-05-02', '82738263827383'),
('ElQaw1cp', 425, 132, 'Credit', 'george', '2027-05-05', '82738263827383'),
('hdsNPPfw', 425, 132, 'Credit', 'looooooooooooo', '2023-05-05', '3343443434343'),
('hEscnijK', 555, 132, 'Credit', 'george', '2027-12-02', '82738263827383'),
('hxibDTGA', 555, 132, 'Credit', 'george', '2023-05-02', '82738263827383'),
('K60lPNN6', 46574, 143, 'Credit', 'george', '2027-12-02', '82738263827383'),
('SRPSW', 7463, 300, 'Debit', 'George El-Hachem', '2027-03-09', '575837425'),
('ttt', 7463, 250, 'Credit', 't', '2028-04-09', '43242341'),
('Yk8YCD7Y', 555, 132, 'Credit', 'george', '2023-05-02', '82738263827383'),
('z0JtgTFG', 555, 132, 'Credit', 'george', '2027-05-02', '82738263827383');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`airline_name`);

--
-- Indexes for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD PRIMARY KEY (`username`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`airplane_id`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`code`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`e_mail`);

--
-- Indexes for table `customer_phone_num`
--
ALTER TABLE `customer_phone_num`
  ADD PRIMARY KEY (`phone_num`,`e_mail`),
  ADD KEY `e_mail` (`e_mail`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`flight_num`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`e_mail`,`ticket_id`),
  ADD KEY `ticket_id` (`ticket_id`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`e_mail`,`flight_num`),
  ADD KEY `flight_num` (`flight_num`);

--
-- Indexes for table `staff_emails`
--
ALTER TABLE `staff_emails`
  ADD PRIMARY KEY (`username`,`e_mail`);

--
-- Indexes for table `staff_phone_numbers`
--
ALTER TABLE `staff_phone_numbers`
  ADD PRIMARY KEY (`username`,`phone_num`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`ticket_id`),
  ADD KEY `flight_num` (`flight_num`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD CONSTRAINT `airline_staff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`);

--
-- Constraints for table `airplane`
--
ALTER TABLE `airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`);

--
-- Constraints for table `customer_phone_num`
--
ALTER TABLE `customer_phone_num`
  ADD CONSTRAINT `customer_phone_num_ibfk_1` FOREIGN KEY (`e_mail`) REFERENCES `customer` (`e_mail`);

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`);

--
-- Constraints for table `purchase`
--
ALTER TABLE `purchase`
  ADD CONSTRAINT `purchase_ibfk_1` FOREIGN KEY (`e_mail`) REFERENCES `customer` (`e_mail`),
  ADD CONSTRAINT `purchase_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`);

--
-- Constraints for table `review`
--
ALTER TABLE `review`
  ADD CONSTRAINT `review_ibfk_1` FOREIGN KEY (`e_mail`) REFERENCES `customer` (`e_mail`),
  ADD CONSTRAINT `review_ibfk_2` FOREIGN KEY (`flight_num`) REFERENCES `flight` (`flight_num`);

--
-- Constraints for table `staff_emails`
--
ALTER TABLE `staff_emails`
  ADD CONSTRAINT `staff_emails_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `staff_phone_numbers`
--
ALTER TABLE `staff_phone_numbers`
  ADD CONSTRAINT `staff_phone_numbers_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`flight_num`) REFERENCES `flight` (`flight_num`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
