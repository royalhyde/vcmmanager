CREATE TABLE `worker_kmc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `ip` varchar(200) DEFAULT NULL,
  `sys` varchar(200) DEFAULT NULL,
  `cpu` int(11) DEFAULT NULL,
  `mem` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `available` int(11) DEFAULT NULL,
  `nance` int(11) DEFAULT NULL,
  `lastreport` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `worker_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `ip` varchar(200) DEFAULT NULL,
  `sys` int(11) DEFAULT NULL,
  `cpu` int(11) DEFAULT NULL,
  `availableInst` varchar(250) DEFAULT NULL,
  `nance` int(11) DEFAULT NULL,
  `lastreport` datetime DEFAULT NULL,
  `mem` int(11) DEFAULT NULL,
  `totalInst` int(11) DEFAULT NULL,
  `spec` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `worker_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `pwd` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


CREATE TABLE `worker_vcms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `server` varchar(200) NOT NULL,
  `busy` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

