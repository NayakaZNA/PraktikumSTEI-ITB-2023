module DeretAritmatika where
 deretAritmatika :: Int -> Int -> Int -> Float
 deretAritmatika n a b = fromIntegral (n * (2 * a + (n - 1) * b)) / 2
