module Fibonacci where
-- Definisi dan Spesifikasi
fibonacci :: Int -> Int
{- Memberikan suku ke-n barisan Fibonacci -}
fibonacci n 
 | n <= 1 = n
 | otherwise = fibonacci (n - 1) + fibonacci (n - 2)