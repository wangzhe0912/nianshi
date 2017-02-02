/*
MySQL Data Transfer
Source Host: localhost
Source Database: nianshi
Target Host: localhost
Target Database: nianshi
Date: 2017/2/2 20:40:45
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for blog
-- ----------------------------
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `content` text,
  `posted_on` datetime DEFAULT NULL,
  `blog_class` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for blog_class
-- ----------------------------
DROP TABLE IF EXISTS `blog_class`;
CREATE TABLE `blog_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blog_class_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `admin` int(11) DEFAULT NULL,
  `shizi` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for video
-- ----------------------------
DROP TABLE IF EXISTS `video`;
CREATE TABLE `video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text,
  `video_class` int(11) DEFAULT NULL,
  `describe` text,
  `posted_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for video_class
-- ----------------------------
DROP TABLE IF EXISTS `video_class`;
CREATE TABLE `video_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_class_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `blog` VALUES ('1', 'asdsad', '<p>asdasdasdas</p><p style=\"line-height: 16px;\"><img src=\"/static/ueditor1_3_6/dialogs/attachment/fileTypeImages/icon_pdf.gif\"/><a href=\"/static/upload/4745cb00-e2f5-11e6-b400-ec55f9f9f3f4.pdf\">10第二部分现代实用深层网络.pdf</a></p><p><br/></p>', '2017-01-25 11:57:26', '1');
INSERT INTO `blog` VALUES ('2', '基础编程1', '<p>asd</p><p><br/></p><p>1</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p>', '2017-01-26 02:36:06', '1');
INSERT INTO `blog` VALUES ('3', '基础编程2', 'asdasd1231<link rel=\"stylesheet\" href=\"../static/css/highlight.css\">', '2017-01-26 07:36:47', '1');
INSERT INTO `blog` VALUES ('4', '阿斯顿', 'asdasd1231<link rel=\"stylesheet\" href=\"../static/css/highlight.css\">', '2017-01-26 15:37:58', '1');
INSERT INTO `blog` VALUES ('5', '123', '<p>asdasd1231王哲</p><link rel=\"stylesheet\" href=\"../static/css/highlight.css\"/>', '2017-01-26 15:40:00', '1');
INSERT INTO `blog` VALUES ('6', 'asd', 'asdasd1231王哲<link rel=\"stylesheet\" href=\"../static/css/highlight.css\">', '2017-01-26 15:44:18', '1');
INSERT INTO `blog` VALUES ('7', 'asda', 'asdasd</p><br/><p>1231</p><br/><p>王哲<link rel=\"stylesheet\" href=\"../static/css/highlight.css\">', '2017-01-26 15:46:44', '1');
INSERT INTO `blog` VALUES ('8', 'deep1', '<p>asdasd</p><br/><p>1231</p><br/><p>王哲<link rel=\"stylesheet\" href=\"../static/css/highlight.css\">', '2017-01-26 15:47:39', '2');
INSERT INTO `blog` VALUES ('9', '测试', '<p>asdasd</p><br/><p>1231</p><br/><p>王哲<link rel=\"stylesheet\" href=\"../static/css/highlight.css\">', '2017-01-26 15:49:20', '3');
INSERT INTO `blog` VALUES ('10', '精品', '<p>asdasd</p><br/><p>1231</p><br/><p>王哲<link rel=\"stylesheet\" href=\"../static/css/highlight.css\">', '2017-01-26 15:49:34', '4');
INSERT INTO `blog` VALUES ('11', '阿瑟大时代', '<p>阿瑟大时代<br/></p>', '2017-01-26 15:50:03', '4');
INSERT INTO `blog` VALUES ('12', '按时打算', '<p>asdasd</p><br/><p>1231</p><br/><p>王哲<link rel=\"stylesheet\" href=\"../static/css/highlight.css\">', '2017-01-26 15:56:56', '1');
INSERT INTO `blog` VALUES ('13', '这是什么？', '<p><span style=\"text-decoration: underline;\">这是一个测试文档！</span><br/></p><p style=\"text-align: center;\">我们希望可以得到一个好的样式。</p><p style=\"text-align: right;\">现在已经4点半多了。</p><p style=\"text-align: right;\"><img src=\"/static/upload/af9d7d80-e3a2-11e6-bfb8-ec55f9f9f3f4.png\" title=\"person.jpg\"/></p>', '2017-01-26 16:37:39', '3');
INSERT INTO `blog` VALUES ('14', 'test', '<p>这是一个测试文档<br/></p><p+style=\"text-align:+center;\">我爱你<br/></p><p+style=\"text-align:+right;\">快要下班啦！<br/></p><p+style=\"text-align:+right;\"><img+width=\"530\"+height=\"340\"+src=\"http://api.map.baidu.com/staticimage?center=116.038354,39.991106&zoom=10&width=530&height=340&markers=115.976263,40.095392\"/><img+src=\"/static/upload/2d75261e-e3a5-11e6-90b2-ec55f9f9f3f4.png\"+title=\"intro-bg.jpg\"/></p>', '2017-01-26 16:55:30', '1');
INSERT INTO `blog` VALUES ('15', '撒多大撒', '<p>按时打算</p><p+style=\"text-align:+center;\">打撒大撒</p><p+style=\"text-align:+right;\">阿斯顿</p>', '2017-01-26 16:58:46', '1');
INSERT INTO `blog` VALUES ('16', 'asa', '<p>阿斯顿</p><p>&nbsp;撒旦</p><p>&nbsp;+&nbsp;阿斯顿</p><p+style=\"text-align:+center;\">阿斯顿<br/></p>', '2017-01-26 16:59:40', '2');
INSERT INTO `blog` VALUES ('17', '打撒', '<p>阿斯顿</p><p>&nbsp; &nbsp;撒旦</p><p style=\"text-align: center;\">阿斯顿<br/></p>', '2017-01-26 17:02:18', '2');
INSERT INTO `blog_class` VALUES ('1', '基础编程');
INSERT INTO `blog_class` VALUES ('2', '深度学习');
INSERT INTO `blog_class` VALUES ('3', '测试相关');
INSERT INTO `blog_class` VALUES ('4', '精品博客');
INSERT INTO `login` VALUES ('1', 'wangzhe', 'qxq102132', '1', '0');
INSERT INTO `login` VALUES ('2', 'shidongli', 'sdl19940208', '0', '1');
