-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 08 Bulan Mei 2021 pada 18.03
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `invetarisasi_barang`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `barang`
--

CREATE TABLE `barang` (
  `ID` varchar(50) NOT NULL,
  `Kode_Barang` varchar(50) NOT NULL,
  `Nama_Barang` char(50) NOT NULL,
  `Merek` varchar(50) NOT NULL,
  `Stock` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `gedung`
--

CREATE TABLE `gedung` (
  `Nama_Gedung` char(20) NOT NULL,
  `ID` varchar(50) NOT NULL,
  `MG_Gedung` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pegawai`
--

CREATE TABLE `pegawai` (
  `NIP_NRK` varchar(50) NOT NULL,
  `Nama_Pegawai` char(50) NOT NULL,
  `Alamat` varchar(50) NOT NULL,
  `No_Telepon` varchar(20) NOT NULL,
  `role` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `peminjaman`
--

CREATE TABLE `peminjaman` (
  `ID` varchar(50) NOT NULL,
  `No_Peminjaman` varchar(50) NOT NULL,
  `NIP_NRK` varchar(50) NOT NULL,
  `Nama_Pegawai` char(50) NOT NULL,
  `Tgl_Pinjam` date NOT NULL,
  `Tgl_Kembali` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `peminjaman_detail`
--

CREATE TABLE `peminjaman_detail` (
  `ID` varchar(50) NOT NULL,
  `No_Peminjaman` varchar(50) NOT NULL,
  `Kode_Barang` varchar(50) NOT NULL,
  `Nama_Barang` char(50) NOT NULL,
  `Jumlah` varchar(10) NOT NULL,
  `Nama_Gedung` char(20) NOT NULL,
  `No_Ruangan` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `ruangan`
--

CREATE TABLE `ruangan` (
  `No_Ruangan` varchar(10) NOT NULL,
  `ID` varchar(50) NOT NULL,
  `Nama_Gedung` char(20) NOT NULL,
  `PJ_Ruangan` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`Kode_Barang`);

--
-- Indeks untuk tabel `gedung`
--
ALTER TABLE `gedung`
  ADD PRIMARY KEY (`Nama_Gedung`);

--
-- Indeks untuk tabel `pegawai`
--
ALTER TABLE `pegawai`
  ADD PRIMARY KEY (`NIP_NRK`);

--
-- Indeks untuk tabel `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD PRIMARY KEY (`No_Peminjaman`),
  ADD KEY `NIP_NRK` (`NIP_NRK`);

--
-- Indeks untuk tabel `peminjaman_detail`
--
ALTER TABLE `peminjaman_detail`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `No_Peminjaman` (`No_Peminjaman`),
  ADD KEY `Kode_Barang` (`Kode_Barang`),
  ADD KEY `No_Ruangan` (`No_Ruangan`),
  ADD KEY `Nama_Gedung` (`Nama_Gedung`);

--
-- Indeks untuk tabel `ruangan`
--
ALTER TABLE `ruangan`
  ADD PRIMARY KEY (`No_Ruangan`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD CONSTRAINT `peminjaman_ibfk_1` FOREIGN KEY (`NIP_NRK`) REFERENCES `pegawai` (`NIP_NRK`);

--
-- Ketidakleluasaan untuk tabel `peminjaman_detail`
--
ALTER TABLE `peminjaman_detail`
  ADD CONSTRAINT `peminjaman_detail_ibfk_1` FOREIGN KEY (`No_Peminjaman`) REFERENCES `peminjaman` (`No_Peminjaman`),
  ADD CONSTRAINT `peminjaman_detail_ibfk_2` FOREIGN KEY (`Kode_Barang`) REFERENCES `barang` (`Kode_Barang`),
  ADD CONSTRAINT `peminjaman_detail_ibfk_3` FOREIGN KEY (`Nama_Gedung`) REFERENCES `gedung` (`Nama_Gedung`) ON UPDATE CASCADE,
  ADD CONSTRAINT `peminjaman_detail_ibfk_4` FOREIGN KEY (`No_Ruangan`) REFERENCES `ruangan` (`No_Ruangan`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
