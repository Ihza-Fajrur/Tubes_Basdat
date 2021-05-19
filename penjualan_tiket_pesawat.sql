-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 19 Bulan Mei 2021 pada 13.22
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 8.0.3

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
-- Struktur dari tabel `cs`
--

CREATE TABLE `cs` (
  `id_cs` varchar(20) NOT NULL,
  `nama_cs` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `cs`
--

INSERT INTO `cs` (`id_cs`, `nama_cs`) VALUES
('APK175', 'Nishimiya'),
('BM154L', 'Redoks'),
('C198KL', 'Muhammad Rifai');

-- --------------------------------------------------------

--
-- Struktur dari tabel `keluhan`
--

CREATE TABLE `keluhan` (
  `no_tiket_keluhan` varchar(10) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Isi_keluhan` varchar(1000) NOT NULL,
  `Balasan` varchar(1000) NOT NULL,
  `ID_CS` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `keluhan`
--

INSERT INTO `keluhan` (`no_tiket_keluhan`, `Username`, `Isi_keluhan`, `Balasan`, `ID_CS`) VALUES
('101361', 'Ihza', 'Delaynya lam nich', 'Keluhan anda belum dibalas, Keluhan anda akan dibalas dalam 3x24 Jam', 'C198KL'),
('101425', 'Ihza', 'Eh udah ngeluh deng', 'Keluhan anda belum dibalas, Keluhan anda akan dibalas dalam 3x24 Jam', 'APK175'),
('101771', 'Ihza', 'Aku harus mengeluh kemana?', 'Keluhan anda belum dibalas, Keluhan anda akan dibalas dalam 3x24 Jam', 'APK175'),
('101974', 'Ihza', 'delay sangat lama', 'Keluhan anda belum dibalas, Keluhan anda akan dibalas dalam 3x24 Jam', 'APK175');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pembeli`
--

CREATE TABLE `pembeli` (
  `kontak` varchar(20) DEFAULT NULL,
  `Username` char(20) NOT NULL,
  `Password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pembeli`
--

INSERT INTO `pembeli` (`kontak`, `Username`, `Password`) VALUES
('0812', 'Ihza', '0'),
('0858', 'Redoqx', 'Rdh');

-- --------------------------------------------------------

--
-- Struktur dari tabel `penjualan_tiket`
--

CREATE TABLE `penjualan_tiket` (
  `no_penjualan` varchar(10) NOT NULL,
  `id_ticketer` varchar(20) NOT NULL,
  `Username` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `penjualan_tiket`
--

INSERT INTO `penjualan_tiket` (`no_penjualan`, `id_ticketer`, `Username`) VALUES
('JLA2178177', 'CVG435', 'Ihza'),
('JLA3848658', 'MNJ169', 'Ihza'),
('JLA4562700', 'CVG435', 'Ihza'),
('JLA4704829', 'BAQL76', 'Ihza'),
('JLA5921989', 'MNJ169', 'Redoqx'),
('JLA6067178', 'BAQL76', 'Ihza'),
('JLA6099167', 'BAQL76', 'Redoqx'),
('JLA6666193', 'MNJ169', 'Ihza'),
('JLA7626795', 'MNJ169', 'Ihza'),
('JLA7691240', 'MNJ169', 'Ihza'),
('JLA9074697', 'BAQL76', 'Ihza');

-- --------------------------------------------------------

--
-- Struktur dari tabel `petugas`
--

CREATE TABLE `petugas` (
  `Id_petugas` varchar(20) NOT NULL,
  `Nama_Petugas` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `petugas`
--

INSERT INTO `petugas` (`Id_petugas`, `Nama_Petugas`) VALUES
('APK175', 'Nishimiya'),
('BAQL76', 'Arima Kousei'),
('BM154L', 'Redoks'),
('C198KL', 'Muhammad Rifai'),
('CVG435', 'Ihza Fajrur'),
('MNJ169', 'Irfan Muksin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `ticketer`
--

CREATE TABLE `ticketer` (
  `id_ticketer` varchar(20) NOT NULL,
  `nama_ticketer` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `ticketer`
--

INSERT INTO `ticketer` (`id_ticketer`, `nama_ticketer`) VALUES
('BAQL76', 'Arima Kousei'),
('CVG435', 'Ihza Fajrur'),
('MNJ169', 'Irfan Muksin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tiket`
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
-- Dumping data untuk tabel `tiket`
--

INSERT INTO `tiket` (`no_tiket`, `no_booking`, `asal`, `tujuan`, `harga`, `no_penjualan`, `tgl_keberangkatan`) VALUES
('Tkt8660909', 'BKG1412702', 'Lampung', 'Pontianak', '1296000', 'JLA3848658', '2021-02-04 00:00:00'),
('Tkt5832734', 'BKG4008827', 'Yogyakarta', 'Bali', '2494000', 'JLA4562700', '2024-02-05 00:00:00'),
('Tkt3565063', 'BKG8296706', 'Pontianak', 'Jakarta', '1450000', 'JLA4704829', '2022-04-06 00:00:00'),
('Tkt1223818', 'BKG3036843', 'Lampung', 'Padang', '648000', 'JLA5921989', '2022-08-06 00:00:00'),
('Tkt5027560', 'BKG6661924', 'Bali', 'Palu', '3082000', 'JLA6099167', '2028-05-06 00:00:00'),
('Tkt3878667', 'BKG9878455', 'Lampung', 'Pontianak', '1296000', 'JLA6666193', '2023-04-30 00:00:00'),
('Tkt6988416', 'BKG9007511', 'Lampung', 'Yogyakarta', '1561000', 'JLA7626795', '2022-09-04 00:00:00'),
('Tkt6600975', 'BKG9113213', 'Lampung', 'Pontianak', '1296000', 'JLA7691240', '2027-05-03 00:00:00'),
('Tkt2708696', 'BKG6031897', 'Jakarta', 'Yogyakarta', '1690000', 'JLA9074697', '2024-04-05 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `cs`
--
ALTER TABLE `cs`
  ADD PRIMARY KEY (`id_cs`);

--
-- Indeks untuk tabel `keluhan`
--
ALTER TABLE `keluhan`
  ADD PRIMARY KEY (`no_tiket_keluhan`),
  ADD KEY `Usename` (`Username`),
  ADD KEY `ID_CS` (`ID_CS`);

--
-- Indeks untuk tabel `pembeli`
--
ALTER TABLE `pembeli`
  ADD PRIMARY KEY (`Username`);

--
-- Indeks untuk tabel `penjualan_tiket`
--
ALTER TABLE `penjualan_tiket`
  ADD PRIMARY KEY (`no_penjualan`),
  ADD KEY `id_ticketer` (`id_ticketer`),
  ADD KEY `Username` (`Username`);

--
-- Indeks untuk tabel `petugas`
--
ALTER TABLE `petugas`
  ADD PRIMARY KEY (`Id_petugas`);

--
-- Indeks untuk tabel `ticketer`
--
ALTER TABLE `ticketer`
  ADD PRIMARY KEY (`id_ticketer`);

--
-- Indeks untuk tabel `tiket`
--
ALTER TABLE `tiket`
  ADD PRIMARY KEY (`no_penjualan`,`no_tiket`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `cs`
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
-- Ketidakleluasaan untuk tabel `keluhan`
--
ALTER TABLE `keluhan`
  ADD CONSTRAINT `keluhan_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `pembeli` (`Username`) ON DELETE CASCADE,
  ADD CONSTRAINT `keluhan_ibfk_2` FOREIGN KEY (`ID_CS`) REFERENCES `cs` (`id_cs`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `penjualan_tiket`
--
ALTER TABLE `penjualan_tiket`
  ADD CONSTRAINT `penjualan_tiket_ibfk_1` FOREIGN KEY (`id_ticketer`) REFERENCES `ticketer` (`id_ticketer`) ON DELETE CASCADE,
  ADD CONSTRAINT `penjualan_tiket_ibfk_2` FOREIGN KEY (`Username`) REFERENCES `pembeli` (`Username`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `ticketer`
--
ALTER TABLE `ticketer`
  ADD CONSTRAINT `ticketer_ibfk_3` FOREIGN KEY (`id_ticketer`) REFERENCES `petugas` (`Id_petugas`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `tiket`
--
ALTER TABLE `tiket`
  ADD CONSTRAINT `tiket_ibfk_1` FOREIGN KEY (`no_penjualan`) REFERENCES `penjualan_tiket` (`no_penjualan`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
