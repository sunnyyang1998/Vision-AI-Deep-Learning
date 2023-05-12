DROP TABLE IF EXISTS `Products`;
CREATE TABLE `Products` (
  `ID` char(128),
  `ProductsID` varchar(128) NOT NULL,
  `Name` varchar(128),
  `Price` int(128),
  `Category` char(128),
  PRIMARY KEY (`ProductsID`)
);

INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('1','scc001','素什锦',12.8,'Signature Chengdu Cuisine');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('2','scc002','一枝独秀',16.8,'Signature Chengdu Cuisine');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('3','scc003','花好月圆',28.5,'Signature Chengdu Cuisine');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('4','scc004','国色天香',48.5,'Signature Chengdu Cuisine');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('5','dds001','冒鸭血',11.8,'Dry Dishes');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('6','dds002','冒小郡肝',13.8,'Dry Dishes');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('7','dds003','冒午餐肉',11.8,'Dry Dishes');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('8','dds004','干拌鹌鹑蛋',8.5,'Dry Dishes');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('9','dds005','干拌金针菇',8.5,'Dry Dishes');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('10','snk001','招牌牛肉面',12.8,'Snack');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('11','snk002','红烧牛腩面',13.8,'Snack');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('12','snk003','麻辣牛肉',13.8,'Snack');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('13','snk004','招牌千层肚',13.8,'Snack');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('14','snk005','招牌猪脑花',13.8,'Snack');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('15','snk006','招牌火锅粉',8.8,'Snack');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('16','brg001','豆奶',3.5,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('17','brg002','加多宝',3.5,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('18','brg003','自制酸梅汤',5,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('19','brg004','可尔必思',3.8,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('20','brg005','矿泉水',2.5,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('21','brg006','北冰洋',3.8,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('22','brg007','可乐',3,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('23','brg008','可乐无糖',3,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('24','brg009','芬达',3,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('25','brg010','雪碧',3,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('26','brg011','康师傅冰红茶',3.8,'Beverages');
INSERT INTO `Products` (`ID`,`ProductsID`,`Name`,`Price`,`Category`) VALUES ('28','brg013','康师傅芒果小酪',3.8,'Beverages');