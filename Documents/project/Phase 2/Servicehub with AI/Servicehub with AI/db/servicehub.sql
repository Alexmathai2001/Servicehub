-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 13, 2022 at 09:48 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `servicehub`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE IF NOT EXISTS `booking` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(20) NOT NULL,
  `bookingdate` date NOT NULL,
  `problem` varchar(300) NOT NULL,
  `status` varchar(30) NOT NULL,
  `userid` int(11) NOT NULL,
  `scid` int(11) NOT NULL,
  `enddate` date NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bid`, `company`, `bookingdate`, `problem`, `status`, `userid`, `scid`, `enddate`) VALUES
(3, 'acer', '2021-01-09', 'battery problem', 'delivered', 7, 2, '2021-01-16'),
(4, 'acer', '2021-01-12', 'battery drain\r\n', 'delivered', 7, 2, '2021-01-12'),
(5, 'asus', '2021-01-07', 'battery problem', 'delivered', 5, 1, '2021-01-14'),
(6, 'asus', '2021-03-11', 'keyboard issue', 'delivered', 6, 3, '2021-03-18'),
(7, 'asus', '2021-04-19', 'mousepad not working', 'complaint registerred', 11, 3, '2021-04-26'),
(8, 'asus', '2022-03-04', 'keybord is not working\r\n', 'delivered', 6, 1, '2022-03-11'),
(9, 'asus', '2022-03-15', 'mouse rewjdhjdhjehgdjeghejfgjegdnsxnxc', 'delivered', 6, 1, '2022-03-22'),
(10, 'apple', '2022-03-15', 'camera', 'delivered', 12, 4, '2022-03-22');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE IF NOT EXISTS `company` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(20) NOT NULL,
  `photo` varchar(300) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`cid`, `companyname`, `photo`) VALUES
(2, 'asus', '/media/download%20(8)_CPTL7f5.jpg'),
(3, 'acer', '/media/ACER.jpg'),
(4, 'dell', '/media/dell.jpg'),
(5, 'apple', '/media/apple.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `faq`
--

CREATE TABLE IF NOT EXISTS `faq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(20) NOT NULL,
  `faq` varchar(100) NOT NULL,
  `answer` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `faq`
--

INSERT INTO `faq` (`id`, `company`, `faq`, `answer`) VALUES
(1, 'asus', 'freequently restarting', 'check software updates'),
(2, 'asus', 'keyboard issues', 'change your keyboard'),
(3, 'apple', 'display', 'replace');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `userid` int(11) NOT NULL,
  `scid` int(11) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fid`, `feedback`, `userid`, `scid`) VALUES
(1, 'very good', 5, 1),
(4, 'very good', 5, 1),
(5, 'feedback..azg', 7, 2),
(6, 'nbad', 7, 2),
(7, 'nbad', 7, 2),
(8, 'good', 5, 1),
(9, 'feedback..sdwsdsd', 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `uname` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `usertype` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uname`, `password`, `usertype`, `status`) VALUES
('binimol1212@gmail.com', 'binimol', 'user', 'approved'),
('admin@gmail.com', 'admin', 'admin', 'approved'),
('arjun@gmail.com', 'arjun', 'servicecenter', 'approved'),
('merin@gmail.com', 'merin', 'user', 'approved'),
('jack123@gmail.com', 'jack1234', 'user', 'approved'),
('apple123@gmail.com', 'apple1234', 'servicecenter', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE IF NOT EXISTS `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(300) NOT NULL,
  `messenger` varchar(50) NOT NULL,
  `recipient` varchar(50) NOT NULL,
  `reply` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`id`, `message`, `messenger`, `recipient`, `reply`) VALUES
(7, 'sdftgyui', 'admin@gmail.com', 'acertech@gmail.com', '');

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE IF NOT EXISTS `question` (
  `qid` int(11) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(30) NOT NULL,
  `product` varchar(30) NOT NULL,
  `questionn` varchar(200) NOT NULL,
  `answer` varchar(250) NOT NULL,
  PRIMARY KEY (`qid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`qid`, `companyname`, `product`, `questionn`, `answer`) VALUES
(2, 'asus', 'laptop', 'restarting frequently', 'check for software update');

-- --------------------------------------------------------

--
-- Table structure for table `screg`
--

CREATE TABLE IF NOT EXISTS `screg` (
  `scid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `address` varchar(20) NOT NULL,
  `phoneno` int(11) NOT NULL,
  `company` varchar(20) NOT NULL,
  `product` varchar(20) NOT NULL,
  `aid` int(11) NOT NULL,
  `password` varchar(20) NOT NULL,
  `district` varchar(20) NOT NULL,
  PRIMARY KEY (`scid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `screg`
--

INSERT INTO `screg` (`scid`, `name`, `email`, `address`, `phoneno`, `company`, `product`, `aid`, `password`, `district`) VALUES
(1, 'arjun', 'arjun@gmail.com', 'medicity ernakulam', 2147483647, 'asus', 'laptop', 12334556, 'arjun', 'ernakulam'),
(3, 'solutions', 's@gmail.com', 'None', 2147483647, 'asus', 'laptop', 123456789, 'solutions', 'ernakulam'),
(4, 'apple', 'apple123@gmail.com', 'california', 2147483647, 'apple', 'iphone', 123456, 'apple1234', 'idukki');

-- --------------------------------------------------------

--
-- Table structure for table `userreg`
--

CREATE TABLE IF NOT EXISTS `userreg` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(30) NOT NULL,
  `phoneno` varchar(15) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `userreg`
--

INSERT INTO `userreg` (`uid`, `name`, `email`, `address`, `phoneno`) VALUES
(5, 'binimol', 'binimol1212@gmail.com', 'sdfghj', '9961630581'),
(6, 'merin', 'merin@gmail.com', 'merin', '2147483647'),
(7, 'SHYAM', 'shyamsasi94@gmal.com', 'dysfsjljscscsojcsc', '2147483647'),
(11, 'anjana', 'anjana@gmail.com', 'anjana home', '1234567890'),
(12, 'jack', 'jack123@gmail.com', 'idukki', '8273999292');
