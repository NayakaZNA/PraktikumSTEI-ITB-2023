module DeretSegitiga where
-- Definisi dan Spesifikasi
    deretSegitiga :: Int -> Int
    {- Menentukan suku ke-n dari suatu deret segitiga -}

-- Realisasi
    deretSegitiga n
     | n == 1 = 1
     | otherwise = n + deretSegitiga (n - 1)
