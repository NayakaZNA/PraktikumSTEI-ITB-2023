module UkuranBaju where

-- Definisi dan Spesifikasi
ukuranBaju :: Int -> Int -> Int
{- Mengklasifikasikan ukuran baju berdasarkan input tinggi badan dan berat badan -}
-- Realisasi
ukuranBaju t b
 | t <= 150 = 1
 | t <= 170 && (b <= 80) = 2
 | t <= 170 = 3
 | b <= 60 = 2
 | b <= 80 = 3
 | otherwise = 4
