CREATE TABLE `sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(50) DEFAULT NULL,
  `start_at` date DEFAULT NULL,
  `end_at` date DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `is_scam` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_url` (`url`) USING BTREE
) DEFAULT CHARSET=utf8;

CREATE TABLE `site_monitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) NOT NULL,
  `monitor` varchar(50) CHARACTER SET utf8 NOT NULL,
  `ref_site_id` int(11) DEFAULT NULL,
  `ref_site_url` varchar(75) CHARACTER SET utf8 DEFAULT NULL,
  `is_paid` tinyint(4) NOT NULL DEFAULT '0',
  `note` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_siteId_monitor` (`site_id`,`monitor`)
) DEFAULT CHARSET=utf8;

CREATE TABLE `unknow_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `monitor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_done` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_url` (`url`)
) DEFAULT CHARSET=utf8;


CREATE TABLE `site_stats` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) DEFAULT NULL,
  `total_account` int(11) DEFAULT NULL,
  `active_account` int(11) DEFAULT NULL,
  `total_deposit` int(11) DEFAULT NULL,
  `total_withdraw` int(11) DEFAULT NULL,
  `time` bigint(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_site_id` (`site_id`)
) DEFAULT CHARSET=utf8;





