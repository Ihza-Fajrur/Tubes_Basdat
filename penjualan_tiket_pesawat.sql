-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2021 at 05:16 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `penjualan_tiket_pesawat`
--

-- --------------------------------------------------------

--
-- Table structure for table `cs`
--

CREATE TABLE `cs` (
  `id_cs` varchar(20) NOT NULL,
  `nama_cs` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cs`
--

INSERT INTO `cs` (`id_cs`, `nama_cs`) VALUES
('APK175', 'Nishimiya'),
('BM154L', 'Redoks'),
('C198KL', 'Muhammad Rifai');

-- --------------------------------------------------------

--
-- Table structure for table `keluhan`
--

CREATE TABLE `keluhan` (
  `no_tiket_keluhan` varchar(10) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Isi_keluhan` varchar(1000) NOT NULL,
  `Balasan` varchar(1000) NOT NULL,
  `ID_CS` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `keluhan`
--

INSERT INTO `keluhan` (`no_tiket_keluhan`, `Username`, `Isi_keluhan`, `Balasan`, `ID_CS`) VALUES
('101589', 'Ihza', 'Testing_3', '', 'BM154L');

-- --------------------------------------------------------

--
-- Table structure for table `pembeli`
--

CREATE TABLE `pembeli` (
  `kontak` varchar(20) DEFAULT NULL,
  `Username` char(20) NOT NULL,
  `Password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pembeli`
--

INSERT INTO `pembeli` (`kontak`, `Username`, `Password`) VALUES
('0812', 'Ihza', '0');

-- --------------------------------------------------------

--
-- Table structure for table `penjualan_tiket`
--

CREATE TABLE `penjualan_tiket` (
  `no_penjualan` varchar(10) NOT NULL,
  `id_ticketer` varchar(20) NOT NULL,
  `Username` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `petugas`
--

CREATE TABLE `petugas` (
  `Id_petugas` varchar(20) NOT NULL,
  `Nama_Petugas` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `petugas`
--

INSERT INTO `petugas` (`Id_petugas`, `Nama_Petugas`) VALUES
('APK175', 'Nishimiya'),
('BAQL76', 'Arima Kousei'),
('BM154L', 'Redoks'),
('C198KL', ' Muhammad Rifai'),
('CVG435', 'Ihza Fajrur'),
('MNJ169', 'Irfan Muksin');

-- --------------------------------------------------------

--
-- Table structure for table `ticketer`
--

CREATE TABLE `ticketer` (
  `id_ticketer` varchar(20) NOT NULL,
  `nama_ticketer` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ticketer`
--

INSERT INTO `ticketer` (`id_ticketer`, `nama_ticketer`) VALUES
('BAQL76', 'Arima Kousei'),
('CVG435', 'Ihza Fajrur'),
('MNJ169', 'Irfan Muksin');

-- --------------------------------------------------------

--
-- Table structure for table `tiket`
--

CREATE TABLE `tiket` (
  `no_tiket` varchar(10) NOT NULL,
  `no_booking` varchar(10) DEFAULT NULL,
  `asal` varchar(20) DEFAULT NULL,
  `tujuan` varchar(20) DEFAULT NULL,
  `harga` varchar(11) DEFAULT NULL,
  `no_penjualan` varchar(10) NOT NULL,
  `tgl_keberangkatan` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cs`
--
ALTER TABLE `cs`
  ADD PRIMARY KEY (`id_cs`);

--
-- Indexes for table `keluhan`
--
ALTER TABLE `keluhan`
  ADD PRIMARY KEY (`no_tiket_keluhan`),
  ADD KEY `Usename` (`Username`),
  ADD KEY `ID_CS` (`ID_CS`);

--
-- Indexes for table `pembeli`
--
ALTER TABLE `pembeli`
  ADD PRIMARY KEY (`Username`);

--
-- Indexes for table `penjualan_tiket`
--
ALTER TABLE `penjualan_tiket`
  ADD PRIMARY KEY (`no_penjualan`),
  ADD KEY `id_ticketer` (`id_ticketer`),
  ADD KEY `Username` (`Username`);

--
-- Indexes for table `petugas`
--
ALTER TABLE `petugas`
  ADD PRIMARY KEY (`Id_petugas`);

--
-- Indexes for table `ticketer`
--
ALTER TABLE `ticketer`
  ADD PRIMARY KEY (`id_ticketer`);

--
-- Indexes for table `tiket`
--
ALTER TABLE `tiket`
  ADD PRIMARY KEY (`no_penjualan`,`no_tiket`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cs`
--
ALTER TABLE `cs`
  ADD CONSTRAINT `cs_ibfk_1` FOREIGN KEY (`id_cs`) REFERENCES `petugas` (`Id_petugas`) ON DELETE CASCADE,
  ADD CONSTRAINT `cs_ibfk_2` FOREIGN KEY (`id_cs`) REFERENCES `petugas` (`Id_petugas`),
  ADD CONSTRAINT `cs_ibfk_3` FOREIGN KEY (`id_cs`) REFERENCES `petugas` (`Id_petugas`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cs_ibfk_4` FOREIGN KEY (`id_cs`) REFERENCES `petugas` (`Id_petugas`),
  ADD CONSTRAINT `cs_ibfk_5` FOREIGN KEY (`id_cs`) REFERENCES `petugas` (`Id_petugas`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cs_ibfk_6` FOREIGN KEY (`id_cs`) REFERENCES `petugas` (`Id_petugas`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cs_ibfk_7` FOREIGN KEY (`id_cs`) REFERENCES `petugas` (`Id_petugas`) ON UPDATE CASCADE;

--
-- Constraints for table `keluhan`
--
ALTER TABLE `keluhan`
  ADD CONSTRAINT `keluhan_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `pembeli` (`Username`) ON DELETE CASCADE,
  ADD CONSTRAINT `keluhan_ibfk_2` FOREIGN KEY (`ID_CS`) REFERENCES `cs` (`id_cs`) ON DELETE CASCADE;

--
-- Constraints for table `penjualan_tiket`
--
ALTER TABLE `penjualan_tiket`
  ADD CONSTRAINT `penjualan_tiket_ibfk_1` FOREIGN KEY (`id_ticketer`) REFERENCES `ticketer` (`id_ticketer`) ON DELETE CASCADE,
  ADD CONSTRAINT `penjualan_tiket_ibfk_2` FOREIGN KEY (`Username`) REFERENCES `pembeli` (`Username`) ON DELETE CASCADE;

--
-- Constraints for table `ticketer`
--
ALTER TABLE `ticketer`
  ADD CONSTRAINT `ticketer_ibfk_3` FOREIGN KEY (`id_ticketer`) REFERENCES `petugas` (`Id_petugas`) ON DELETE CASCADE;

--
-- Constraints for table `tiket`
--
ALTER TABLE `tiket`
  ADD CONSTRAINT `tiket_ibfk_1` FOREIGN KEY (`no_penjualan`) REFERENCES `penjualan_tiket` (`no_penjualan`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
