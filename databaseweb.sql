-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2015-04-02 08:06:09
-- 服务器版本： 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `databaseweb`
--

-- --------------------------------------------------------

--
-- 表的结构 `command_data`
--

CREATE TABLE IF NOT EXISTS `command_data` (
  `id` varchar(50) NOT NULL,
  `task_id` varchar(50) NOT NULL,
  `raw_data_id` varchar(50) NOT NULL,
  `nameID` varchar(20) DEFAULT NULL,
  `valuetype` varchar(20) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `unit` varchar(20) DEFAULT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `raw_data`
--

CREATE TABLE IF NOT EXISTS `raw_data` (
  `id` varchar(50) NOT NULL DEFAULT '',
  `task_id` varchar(50) NOT NULL,
  `value` blob,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `raw_data`
--

INSERT INTO `raw_data` (`id`, `task_id`, `value`, `time`) VALUES
('wwwww', '1', NULL, '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- 表的结构 `response_data`
--

CREATE TABLE IF NOT EXISTS `response_data` (
  `id` varchar(50) NOT NULL,
  `task_id` varchar(50) NOT NULL,
  `raw_data_id` varchar(50) NOT NULL,
  `nameID` varchar(20) DEFAULT NULL,
  `valuetype` varchar(20) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `unit` varchar(20) DEFAULT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `task`
--

CREATE TABLE IF NOT EXISTS `task` (
  `id` varchar(50) NOT NULL,
  `taskname` varchar(20) DEFAULT NULL,
  `attribute` varchar(20) DEFAULT NULL,
  `explanation` varchar(255) DEFAULT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime DEFAULT NULL,
  `profile` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `task`
--

INSERT INTO `task` (`id`, `taskname`, `attribute`, `explanation`, `start_time`, `end_time`, `profile`) VALUES
('001427810957260daf71aae7ca3447f84c346f2a05d7dda000', '1', '', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 'telemetry_data');

-- --------------------------------------------------------

--
-- 表的结构 `telemetry_data`
--

CREATE TABLE IF NOT EXISTS `telemetry_data` (
  `id` varchar(50) NOT NULL,
  `task_id` varchar(50) NOT NULL,
  `raw_data_id` varchar(50) NOT NULL,
  `nameID` varchar(20) DEFAULT NULL,
  `valuetype` varchar(20) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `unit` varchar(20) DEFAULT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` varchar(50) NOT NULL,
  `username` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `username`) VALUES
('1', 'yuanjiace');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `command_data`
--
ALTER TABLE `command_data`
 ADD PRIMARY KEY (`id`), ADD KEY `task_id` (`task_id`), ADD KEY `raw_data_id` (`raw_data_id`);

--
-- Indexes for table `raw_data`
--
ALTER TABLE `raw_data`
 ADD PRIMARY KEY (`id`), ADD KEY `task_id` (`task_id`);

--
-- Indexes for table `response_data`
--
ALTER TABLE `response_data`
 ADD PRIMARY KEY (`id`), ADD KEY `task_id` (`task_id`), ADD KEY `raw_data_id` (`raw_data_id`);

--
-- Indexes for table `task`
--
ALTER TABLE `task`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `telemetry_data`
--
ALTER TABLE `telemetry_data`
 ADD PRIMARY KEY (`id`), ADD KEY `task_id` (`task_id`), ADD KEY `raw_data_id` (`raw_data_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `username` (`username`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
