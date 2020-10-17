-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2020-10-15 17:38:31
-- 服务器版本： 5.6.49-log
-- PHP 版本： 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `picSpider`
--

-- --------------------------------------------------------

--
-- 表的结构 `atr`
--

CREATE TABLE `atr` (
  `id` int(11) NOT NULL,
  `lastUpdate` datetime NOT NULL,
  `numOfMobile` int(11) NOT NULL,
  `numOfPC` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `atr`
--

INSERT INTO `atr` (`id`, `lastUpdate`, `numOfMobile`, `numOfPC`) VALUES
(0, '2020-10-15 13:54:13', 0, 0);

-- --------------------------------------------------------

--
-- 表的结构 `picm`
--

CREATE TABLE `picm` (
  `id` int(11) NOT NULL,
  `originalID` int(11) NOT NULL,
  `URL` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `picm`
--

INSERT INTO `picm` (`id`, `originalID`, `URL`) VALUES
(0, 0, 'https://hlz.ink');

-- --------------------------------------------------------

--
-- 表的结构 `picpc`
--

CREATE TABLE `picpc` (
  `id` int(11) NOT NULL,
  `originalID` int(11) NOT NULL,
  `URL` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `picpc`
--

INSERT INTO `picpc` (`id`, `originalID`, `URL`) VALUES
(0, 0, 'https://hlz.ink');

--
-- 转储表的索引
--

--
-- 表的索引 `atr`
--
ALTER TABLE `atr`
  ADD UNIQUE KEY `id` (`id`);

--
-- 表的索引 `picm`
--
ALTER TABLE `picm`
  ADD UNIQUE KEY `id_2` (`id`);

--
-- 表的索引 `picpc`
--
ALTER TABLE `picpc`
  ADD UNIQUE KEY `id_2` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
