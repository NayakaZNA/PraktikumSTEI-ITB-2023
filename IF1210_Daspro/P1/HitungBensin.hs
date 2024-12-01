module HitungBensin where

-- Definisi dan Spesifikasi
hitungKonsumsiBensin :: Int -> Int
{- Menentukan banyaknya bensin yang dikonsumsi dari suatu titik tertentu sampai 1. -}

-- Realisasi
hitungKonsumsiBensin titik
 | titik == 1 = 0
 | even titik = 1 + hitungKonsumsiBensin (div titik 2)
 | otherwise = 1 + hitungKonsumsiBensin (3 * titik + 1)

-- Definisi dan Spesifikasi
hitungBensin :: Int -> Int -> Int
{- Menentukan total bensin yang dikonsumsi untuk tiap perjalanan yang di mulai di titik A hingga yang dimulai di titik B -}

-- Realisasi
hitungBensin a b
 | a == b + 1 = 0 -- Berhenti pada ujung akhir interval
 | otherwise = hitungKonsumsiBensin a + hitungBensin (a + 1) b
