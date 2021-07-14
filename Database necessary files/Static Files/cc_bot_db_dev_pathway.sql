-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: cc-bot-db-dev.cf7dst2xoq2g.us-east-2.rds.amazonaws.com    Database: cc_bot_db_dev
-- ------------------------------------------------------
-- Server version	8.0.17

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- Table structure for table `pathway`
--

DROP TABLE IF EXISTS `pathway`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pathway` (
  `pathway_id` int(10) unsigned NOT NULL,
  `name` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `campus_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `url` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `img_url` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`pathway_id`),
  UNIQUE KEY `idpathway_UNIQUE` (`pathway_id`),
  KEY `fk_pathway_campus` (`campus_id`),
  CONSTRAINT `fk_pathway_campus` FOREIGN KEY (`campus_id`) REFERENCES `campus` (`campus_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pathway`
--

LOCK TABLES `pathway` WRITE;
/*!40000 ALTER TABLE `pathway` DISABLE KEYS */;
INSERT INTO `pathway` VALUES (1,'College of Community Studies and Public Affairs','76','https://www.metrostate.edu/academics/community-studies',''),(2,'College of Individualized Studies','76','https://www.metrostate.edu/academics/individualized-studies',''),(3,'College of Liberal Arts','76','https://www.metrostate.edu/academics/liberal-arts',''),(4,'College of Management','76','https://www.metrostate.edu/academics/management',''),(5,'College of Sciences','76','https://www.metrostate.edu/academics/sciences',''),(6,'College of Nursing and Health Sciences','76','https://www.metrostate.edu/academics/nursing-and-health-sciences',''),(7,'School of Urban Education','76','https://www.metrostate.edu/academics/urban-education',''),(8,'Applied Design Pathway','304','https://www.century.edu/academics/programs-degrees?field_program_pathway_ref_tid[]=2501',' '),(9,'Arts & Humanities Pathway','304','https://www.century.edu/academics/programs-degrees?field_program_pathway_ref_tid[]=871',' '),(10,'Business Pathway','304','https://www.century.edu/academics/programs-degrees?field_program_pathway_ref_tid[]=881',' '),(11,'Health Sciences Pathway','304','https://www.century.edu/academics/programs-degrees?field_program_pathway_ref_tid[]=891',' '),(12,'Human Services Pathway','304','https://www.century.edu/academics/programs-degrees?field_program_pathway_ref_tid[]=886',' '),(13,'Industry Pathway','304','https://www.century.edu/academics/programs-degrees?field_program_pathway_ref_tid[]=876',' '),(14,'Science, Technology, Engineering & Mathematics Pathway','304','https://www.century.edu/academics/programs-degrees?field_program_pathway_ref_tid[]=896',' '),(15,'Social & Behavioral Sciences Pathway','304','https://www.century.edu/academics/programs-degrees?field_program_pathway_ref_tid[]=2506','  '),(16,'College of Liberal Arts','73','https://www.stcloudstate.edu/cla/default.aspx',' '),(17,'School of the Arts','73','https://www.stcloudstate.edu/sota/default.aspx',' '),(18,'Herberger Business School','73','https://www.stcloudstate.edu/hbs/default.aspx',' '),(19,'College of Science and Engineering','73','https://www.stcloudstate.edu/cose/default.aspx',' '),(20,'School of Computing, Engineering and Environment','73','https://www.stcloudstate.edu/cose/about-college/scee.aspx',' '),(21,'School of Education','73','https://www.stcloudstate.edu/soe/default.aspx',' '),(22,'School of Health and Human Services','73','https://www.stcloudstate.edu/shhs/default.aspx',' ');
/*!40000 ALTER TABLE `pathway` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-10 19:10:03
