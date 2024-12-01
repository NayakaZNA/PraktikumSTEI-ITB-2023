module KonversiSuhu where
-- Definisi dan Spesifikasi
konversiSuhu :: Float -> Char -> Float
{- Mengkonversi temperatur ke satuan lainnya -}
-- Realisasi
konversiSuhu t k
 | k == 'R' = 4/5 * t
 | k == 'F' = 9/5 * t + 32
 | otherwise = t + 273.15