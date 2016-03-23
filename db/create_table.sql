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
  `monitor` varchar(50) NOT NULL,
  `ref_site_id` int(11) DEFAULT NULL,
  `ref_site_url` varchar(75) DEFAULT NULL,
  `is_paid` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_siteId_monitor` (`site_id`,`monitor`)
) DEFAULT CHARSET=utf8;



ALTER TABLE `sites`
DROP COLUMN `name`;



