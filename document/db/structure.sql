CREATE TABLE `words` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(100) DEFAULT NULL,
  `meaning` varchar(100) DEFAULT NULL,
  `audioPath` varchar(150) DEFAULT NULL,
  `tags` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `words`
ADD COLUMN `category`  varchar(50) NULL AFTER `tags`;

ALTER TABLE `words`
ADD UNIQUE INDEX `text_unique_idx` (`text`) ;

