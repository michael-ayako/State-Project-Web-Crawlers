-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cc_bot_db_dev
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `section` (
  `section_id` int unsigned NOT NULL AUTO_INCREMENT,
  `number` smallint unsigned NOT NULL,
  `campus_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `term` enum('j-term','spring','summer','fall') CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `resident_tuition` float DEFAULT NULL,
  `nonresident_tuition` float DEFAULT NULL,
  `fees` float DEFAULT NULL,
  `course_subject` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `course_number` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `year` year NOT NULL,
  `description` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `url` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `credits` float unsigned DEFAULT NULL,
  `campus` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `offered_through` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `location` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `semester` int NOT NULL,
  PRIMARY KEY (`section_id`),
  UNIQUE KEY `idsection_UNIQUE` (`section_id`),
  KEY `fk_section_course_idx` (`course_subject`,`course_number`),
  KEY `fk_section_campus` (`campus_id`),
  CONSTRAINT `fk_section_campus` FOREIGN KEY (`campus_id`) REFERENCES `campus` (`campus_id`),
  CONSTRAINT `fk_section_course` FOREIGN KEY (`course_subject`, `course_number`) REFERENCES `course` (`subject`, `number`)
) ENGINE=InnoDB AUTO_INCREMENT=62797 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-17 17:40:22
