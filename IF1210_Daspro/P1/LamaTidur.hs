module LamaTidur where

lamaTidur :: Int -> Int -> Int -> (Bool, Int, Int, Int)

lamaTidur j m d =
    (tidurCukup, jam, menit, detik)
    where
        waktuTidur = j * 3600 + m * 60 + d
        waktuBangun = 5 * 3600 -- pukul 05.00

        lamaTidurHariIni
            | j < 5 = waktuBangun - waktuTidur                 -- hari yang sama
            | otherwise = waktuBangun - waktuTidur + 24 * 3600 -- hari kemarin        
        
        -- Konversi hasil ke dalam satuan waktu
        jam = div lamaTidurHariIni 3600
        menit = div (mod lamaTidurHariIni 3600) 60
        detik = mod lamaTidurHariIni 60

        -- Tentukan apakah tidur cukup atau tidak
        tidurCukup = jam >= 6