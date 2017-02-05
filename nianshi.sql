/*
Navicat MySQL Data Transfer

Source Server         : 念师
Source Server Version : 50711
Source Host           : localhost:3306
Source Database       : nianshi

Target Server Type    : MYSQL
Target Server Version : 50711
File Encoding         : 65001

Date: 2017-02-05 17:34:48
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog
-- ----------------------------

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
-- Records of blog_class
-- ----------------------------
INSERT INTO `blog_class` VALUES ('1', '基础编程');
INSERT INTO `blog_class` VALUES ('2', '深度学习');
INSERT INTO `blog_class` VALUES ('3', '测试相关');
INSERT INTO `blog_class` VALUES ('4', '精品博客');

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
-- Records of login
-- ----------------------------
INSERT INTO `login` VALUES ('1', 'wangzhe', 'qxq102132', '1', '0');
INSERT INTO `login` VALUES ('2', 'shidongli', 'sdl19940208', '0', '1');

-- ----------------------------
-- Table structure for resource
-- ----------------------------
DROP TABLE IF EXISTS `resource`;
CREATE TABLE `resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of resource
-- ----------------------------
INSERT INTO `resource` VALUES ('1', '112', '1');
INSERT INTO `resource` VALUES ('2', '112', '1');
INSERT INTO `resource` VALUES ('3', '112', '1');
INSERT INTO `resource` VALUES ('4', '112', '1');
INSERT INTO `resource` VALUES ('5', '112', '1');
INSERT INTO `resource` VALUES ('6', '112', '1');
INSERT INTO `resource` VALUES ('7', '112', '1');
INSERT INTO `resource` VALUES ('8', '112', '1');
INSERT INTO `resource` VALUES ('9', '', '');
INSERT INTO `resource` VALUES ('10', '', '');
INSERT INTO `resource` VALUES ('11', '', '');
INSERT INTO `resource` VALUES ('12', 'url', '123');
INSERT INTO `resource` VALUES ('13', '312', '13');
INSERT INTO `resource` VALUES ('14', '312', '131');
INSERT INTO `resource` VALUES ('15', '312', '13');
INSERT INTO `resource` VALUES ('16', '312', '13');
INSERT INTO `resource` VALUES ('17', '112', '1');
INSERT INTO `resource` VALUES ('18', '112', '1');
INSERT INTO `resource` VALUES ('19', '112', '1');
INSERT INTO `resource` VALUES ('20', '112', '1');
INSERT INTO `resource` VALUES ('21', '1', '1');
INSERT INTO `resource` VALUES ('22', '1', '1');
INSERT INTO `resource` VALUES ('23', '1', '1');
INSERT INTO `resource` VALUES ('24', '1', '1');
INSERT INTO `resource` VALUES ('25', '231', '213');
INSERT INTO `resource` VALUES ('26', '耳温枪', '额外');
INSERT INTO `resource` VALUES ('27', '耳温枪', '额外');
INSERT INTO `resource` VALUES ('28', '阿斯顿', '阿斯顿');
INSERT INTO `resource` VALUES ('29', '十大', '撒旦');
INSERT INTO `resource` VALUES ('30', '十大', '撒旦撒旦');

-- ----------------------------
-- Table structure for tool
-- ----------------------------
DROP TABLE IF EXISTS `tool`;
CREATE TABLE `tool` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text,
  `tool_class` int(11) DEFAULT NULL,
  `detail` text,
  `posted_on` datetime DEFAULT NULL,
  `resource_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `resouce` (`resource_id`) USING BTREE,
  CONSTRAINT `tool_ibfk_1` FOREIGN KEY (`resource_id`) REFERENCES `resource` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tool
-- ----------------------------

-- ----------------------------
-- Table structure for tool_class
-- ----------------------------
DROP TABLE IF EXISTS `tool_class`;
CREATE TABLE `tool_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tool_class_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tool_class
-- ----------------------------
INSERT INTO `tool_class` VALUES ('1', '软件');
INSERT INTO `tool_class` VALUES ('2', '书籍');
INSERT INTO `tool_class` VALUES ('3', 'AI应用');
INSERT INTO `tool_class` VALUES ('4', '深度学习训练集');

-- ----------------------------
-- Table structure for video
-- ----------------------------
DROP TABLE IF EXISTS `video`;
CREATE TABLE `video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text,
  `video_class` int(11) DEFAULT NULL,
  `detail` text,
  `posted_on` datetime DEFAULT NULL,
  `resource_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `resouce` (`resource_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of video
-- ----------------------------

-- ----------------------------
-- Table structure for video_class
-- ----------------------------
DROP TABLE IF EXISTS `video_class`;
CREATE TABLE `video_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_class_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of video_class
-- ----------------------------
INSERT INTO `video_class` VALUES ('1', 'Python课程');
INSERT INTO `video_class` VALUES ('2', '数据库相关课程');
INSERT INTO `video_class` VALUES ('3', '深度学习课程');
INSERT INTO `video_class` VALUES ('4', '前端技术课程');
INSERT INTO `video_class` VALUES ('5', '测试相关课程');
