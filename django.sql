-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table django.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.auth_group: ~0 rows (approximately)

-- Dumping structure for table django.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.auth_group_permissions: ~0 rows (approximately)

-- Dumping structure for table django.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.auth_permission: ~35 rows (approximately)
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(25, 'Can add movie', 7, 'add_movie');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(26, 'Can change movie', 7, 'change_movie');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(27, 'Can delete movie', 7, 'delete_movie');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(28, 'Can view movie', 7, 'view_movie');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(29, 'Can add stream platform', 8, 'add_streamplatform');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(30, 'Can change stream platform', 8, 'change_streamplatform');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(31, 'Can delete stream platform', 8, 'delete_streamplatform');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(32, 'Can view stream platform', 8, 'view_streamplatform');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(33, 'Can add watch list', 9, 'add_watchlist');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(34, 'Can change watch list', 9, 'change_watchlist');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(35, 'Can delete watch list', 9, 'delete_watchlist');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(36, 'Can view watch list', 9, 'view_watchlist');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(37, 'Can add review', 10, 'add_review');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(38, 'Can change review', 10, 'change_review');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(39, 'Can delete review', 10, 'delete_review');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(40, 'Can view review', 10, 'view_review');

-- Dumping structure for table django.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.auth_user: ~0 rows (approximately)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$390000$EQV8AgqRKu8qEotv85rpLb$Oo7R3lARuNx0//FWb313VIiPUh31PbNcp9CJUi42RwY=', '2023-06-19 02:25:33.696446', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2023-06-13 09:02:32.490987');

-- Dumping structure for table django.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.auth_user_groups: ~0 rows (approximately)

-- Dumping structure for table django.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.auth_user_user_permissions: ~0 rows (approximately)

-- Dumping structure for table django.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.django_admin_log: ~4 rows (approximately)
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2023-06-13 10:01:40.068975', '1', 'id:1 name:Python Best', 1, '[{"added": {}}]', 7, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(2, '2023-06-14 08:00:09.614946', '1', 'id:1 name:Avatar', 1, '[{"added": {}}]', 9, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(3, '2023-06-14 08:07:03.561771', '1', 'id:1 name:netflix', 1, '[{"added": {}}]', 8, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(4, '2023-06-14 08:08:09.298011', '1', 'id:1 name:netflix', 2, '[{"changed": {"fields": ["Website"]}}]', 8, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(5, '2023-06-19 02:26:35.572357', '1', 'id:1 rating:4 watchlist', 1, '[{"added": {}}]', 10, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(6, '2023-06-19 10:09:25.372063', '2', 'id:2 name:jujutsu kaisen', 1, '[{"added": {}}]', 9, 1);

-- Dumping structure for table django.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.django_content_type: ~9 rows (approximately)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(3, 'auth', 'group');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(2, 'auth', 'permission');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(4, 'auth', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(6, 'sessions', 'session');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(7, 'watchlist_app', 'movie');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(10, 'watchlist_app', 'review');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(8, 'watchlist_app', 'streamplatform');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(9, 'watchlist_app', 'watchlist');

-- Dumping structure for table django.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.django_migrations: ~20 rows (approximately)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2023-06-13 09:00:12.540222');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(2, 'auth', '0001_initial', '2023-06-13 09:00:12.841411');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(3, 'admin', '0001_initial', '2023-06-13 09:00:12.933197');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(4, 'admin', '0002_logentry_remove_auto_add', '2023-06-13 09:00:12.940707');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-06-13 09:00:12.947747');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(6, 'contenttypes', '0002_remove_content_type_name', '2023-06-13 09:00:13.002367');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(7, 'auth', '0002_alter_permission_name_max_length', '2023-06-13 09:00:13.044442');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(8, 'auth', '0003_alter_user_email_max_length', '2023-06-13 09:00:13.066365');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(9, 'auth', '0004_alter_user_username_opts', '2023-06-13 09:00:13.072907');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(10, 'auth', '0005_alter_user_last_login_null', '2023-06-13 09:00:13.112536');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(11, 'auth', '0006_require_contenttypes_0002', '2023-06-13 09:00:13.114682');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(12, 'auth', '0007_alter_validators_add_error_messages', '2023-06-13 09:00:13.120681');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(13, 'auth', '0008_alter_user_username_max_length', '2023-06-13 09:00:13.164880');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(14, 'auth', '0009_alter_user_last_name_max_length', '2023-06-13 09:00:13.209923');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(15, 'auth', '0010_alter_group_name_max_length', '2023-06-13 09:00:13.229457');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(16, 'auth', '0011_update_proxy_permissions', '2023-06-13 09:00:13.237032');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(17, 'auth', '0012_alter_user_first_name_max_length', '2023-06-13 09:00:13.296202');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(18, 'sessions', '0001_initial', '2023-06-13 09:00:13.315631');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(19, 'watchlist_app', '0001_initial', '2023-06-13 09:00:13.327908');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(20, 'watchlist_app', '0002_streamplatform_watchlist', '2023-06-14 07:57:28.802106');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(21, 'watchlist_app', '0003_alter_streamplatform_website', '2023-06-14 08:09:21.184676');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(22, 'watchlist_app', '0004_watchlist_platform', '2023-06-15 04:25:21.656212');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(23, 'watchlist_app', '0005_review', '2023-06-19 02:23:48.973456');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(24, 'watchlist_app', '0006_review_user_alter_review_watchlist', '2023-07-24 02:15:30.995777');

-- Dumping structure for table django.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.django_session: ~2 rows (approximately)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('dsnnr1l1zj4s2vwf45t9j7u8wy8me28z', '.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MwkO_1uCfKD2g7wDu3Wee5tXebEd4UfdPBrR3peDvfvoMKo31qBtoEAivaYgnGkdPIhT458RnSaVJk0Cu-FxyyTNBZVVkVZK4Qhkdj7A_XEOAo:1q90ps:0EUApv6xWSp3lPdbcTT3JVYKc_98h-3ReMeDv68tGgs', '2023-06-27 10:01:12.635989');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('n5x0k12j795nwumcgsonp8ivslcb8a58', '.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MwkO_1uCfKD2g7wDu3Wee5tXebEd4UfdPBrR3peDvfvoMKo31qBtoEAivaYgnGkdPIhT458RnSaVJk0Cu-FxyyTNBZVVkVZK4Qhkdj7A_XEOAo:1qB4aD:hEAycq4PIS07qvIH2bodLmAxf8TYevjcZFwpBfhLNUw', '2023-07-03 02:25:33.749990');

-- Dumping structure for table django.watchlist_app_movie
CREATE TABLE IF NOT EXISTS `watchlist_app_movie` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `movie_name` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `status_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.watchlist_app_movie: ~1 rows (approximately)
INSERT INTO `watchlist_app_movie` (`id`, `movie_name`, `description`, `status_active`) VALUES
	(1, 'Python Best2 s', 'jajaj', 1);

-- Dumping structure for table django.watchlist_app_review
CREATE TABLE IF NOT EXISTS `watchlist_app_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` int unsigned DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `update` datetime(6) NOT NULL,
  `watchlist_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `watchlist_app_review_watchlist_id_64edfa69_fk_watchlist` (`watchlist_id`),
  KEY `watchlist_app_review_user_id_2fc96425_fk_auth_user_id` (`user_id`),
  CONSTRAINT `watchlist_app_review_user_id_2fc96425_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `watchlist_app_review_watchlist_id_64edfa69_fk_watchlist` FOREIGN KEY (`watchlist_id`) REFERENCES `watchlist_app_watchlist` (`id`),
  CONSTRAINT `watchlist_app_review_chk_1` CHECK ((`rating` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.watchlist_app_review: ~5 rows (approximately)
INSERT INTO `watchlist_app_review` (`id`, `rating`, `description`, `active`, `created`, `update`, `watchlist_id`, `user_id`) VALUES
	(1, 4, 'ddd', 1, '2023-06-19 02:26:35.571357', '2023-06-19 02:26:35.571357', 1, 1);
INSERT INTO `watchlist_app_review` (`id`, `rating`, `description`, `active`, `created`, `update`, `watchlist_id`, `user_id`) VALUES
	(3, 1, 'baik', 1, '2023-06-19 10:08:53.260335', '2023-06-19 10:08:53.260335', 1, 1);
INSERT INTO `watchlist_app_review` (`id`, `rating`, `description`, `active`, `created`, `update`, `watchlist_id`, `user_id`) VALUES
	(4, 2, 'asdad', 0, '2023-06-20 08:58:59.583156', '2023-06-20 08:58:59.583156', 1, 1);
INSERT INTO `watchlist_app_review` (`id`, `rating`, `description`, `active`, `created`, `update`, `watchlist_id`, `user_id`) VALUES
	(5, 2, '333', 0, '2023-06-20 09:02:31.076050', '2023-06-20 09:02:31.076050', 1, 1);
INSERT INTO `watchlist_app_review` (`id`, `rating`, `description`, `active`, `created`, `update`, `watchlist_id`, `user_id`) VALUES
	(6, 5, '123213', 0, '2023-06-20 09:04:39.387657', '2023-06-20 09:04:39.387657', 1, 1);

-- Dumping structure for table django.watchlist_app_streamplatform
CREATE TABLE IF NOT EXISTS `watchlist_app_streamplatform` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `about` varchar(150) NOT NULL,
  `website` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.watchlist_app_streamplatform: ~9 rows (approximately)
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(2, 'disney', 'best', 'https://disney.com');
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(3, 'netflix', 'best', 'https://netflix.com');
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(4, 'prime', 'best', 'https://netflix.com');
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(5, 'viu', 'best', 'https://netflix.com');
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(6, 'HBO', 'best', 'https://netflix.com');
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(7, 'HBO', 'best', 'https://netflix.com');
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(8, 'HBO by custom create2', 'best', 'https://netflix.com');
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(9, 'adasdasd', 'adsad', 'https://google.com');
INSERT INTO `watchlist_app_streamplatform` (`id`, `name`, `about`, `website`) VALUES
	(10, 'HBO by model view set', 'HBO by model view set', 'https://hbo.com');

-- Dumping structure for table django.watchlist_app_watchlist
CREATE TABLE IF NOT EXISTS `watchlist_app_watchlist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `storyline` varchar(500) NOT NULL,
  `status_active` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `platform_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `watchlist_app_watchl_platform_id_93eea261_fk_watchlist` (`platform_id`),
  CONSTRAINT `watchlist_app_watchl_platform_id_93eea261_fk_watchlist` FOREIGN KEY (`platform_id`) REFERENCES `watchlist_app_streamplatform` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table django.watchlist_app_watchlist: ~2 rows (approximately)
INSERT INTO `watchlist_app_watchlist` (`id`, `title`, `storyline`, `status_active`, `created`, `platform_id`) VALUES
	(1, 'Avatar', 'Blue Avatar\'s', 1, '2023-06-14 08:00:09.611945', 2);
INSERT INTO `watchlist_app_watchlist` (`id`, `title`, `storyline`, `status_active`, `created`, `platform_id`) VALUES
	(2, 'jujutsu kaisen', 'asadadsas', 1, '2023-06-19 10:09:25.369633', 2);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
