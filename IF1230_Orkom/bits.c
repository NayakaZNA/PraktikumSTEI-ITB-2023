#include <stdio.h>

/**
 * NAMA     : Z. Nayaka Athadiansyah
 * NIM      : 13523094
 * KELAS    : IF2
 * 
 * 
 * Aturan Coding Soal Integer
 * Kode harus mengikuti style:
 * int var1 = Expr1;
 * ...
 * int varX = ExprX;
 * varY = ExprY;
 * ...
 * varZ = ExprZ;
 * return ExprR;
 * 
 * Setiap "Expr" adalah ekspresi HANYA menggunakan:
 * 1. Konstanta 0 hingga 255 (0xFF), inklusif. Anda tidak diperbolehkan 
 * untuk menggunakan konstanta besar seperti 0xffffffff kecuali dituliskan
 * pada soal.
 * 2. Argumen fungsi dan variabel lokal (tidak ada variabel global).
 * 3. Operasi integer uner ! ~
 * 4. Operasi integer biner & ^ | + << >>
 * 
 * Beberapa soal merestriksi jumlah operator. Setiap "Expr" terdiri
 * atas beberapa operator. Anda tidak dibatasi oleh 1 operator per baris.
 * 
 * Anda sangat dilarang untuk:
 * 1. Menggunakan control constructs apapun, seperti if, do, while, for, switch, dll.
 * 2. Menggunakan macro.
 * 3. Membuat fungsi baru di file ini.
 * 4. Memanggil fungsi lain.
 * 5. Menggunakan operasi lain, seperti &&, ||, -, atau ?:
 * 6. Menggunakan bentuk casting apapun.
 * 7. Menggunakan tipe data selain int. Ini berarti Anda tidak boleh menggunakan
 * array, struct, atau union.
 * 
 * Anda dapat berasumsi mesin Anda:
 * 1. Menggunakan 2s complement, representasi bilangan 32-bit.
 * 2. Mengeksekusi right shift (>>) secara aritmetik.
 * 3. Memiliki perilaku unpredictable ketika menggeser integer lebih dari ukuran word.
 * 
 * Aturan Coding Soal Float
 * 
 * Untuk soal yang membutuhkan operasi floating-point, style koding lebih lenient.
 * Anda diperbolehkan menggunakan ints dan unsigneds. Anda dapat menggunakan
 * arbitrary integer dan konstanta unsigned.
 * 
 * Anda sangat dilarang untuk:
 * 1. Menggunakan macro.
 * 2. Membuat fungsi baru di file ini.
 * 3. Memanggil fungsi lain.
 * 4. Menggunakan bentuk casting apapun.
 * 5. Menggunakan tipe data selain int atau unsigned. Ini berarti Anda tidak boleh menggunakan
 * 6. Menggunakan floating point apapun untuk tipe data, operasi, atau konstanta.
 * 
 * NOTES
 * Setiap fungsi memiliki jumlah operator maksimum/max ops yang boleh digunakan
 * untuk mengimplementasikan fungsi.
 * '=' tidak dihitung dan dapat digunakan sebanyak apapun tanpa penalti.
 */



// Soal 1
/**
 * chicken_or_beef - Ekstrak 4 bit kedua dari chicken dan ekstrak 4 bit pertama dari beef*2, 
 * kemudian gabungkan dengan bitwise OR.
 * 
 * (Di sini, 4 bit pertama artinya 4 bit paling kanan, yaitu bit ke-0 hingga ke-3
 * dan 4 bit kedua artinya 4 bit setelahnya, yaitu bit ke-4 hingga ke-7)
 * 
 * Contoh:
 * chicken_or_beef(0b10010101, 0b11111000) = 0b1001
 * chicken_or_beef(0b01010000, 0b10001101) = 0b1111
 * chicken_or_beef(0b01100000, 0b11111111) = 0b1110
 * 
 * Legal ops    : << >> | &
 * Max ops      : 5
 * Rating       : 1
 */
int chicken_or_beef(int chicken, int beef) {
    beef = (beef << 1) & 15;
    chicken = (chicken >> 4) & 15;
    return chicken | beef;
}

// Soal 2
/**
 * masquerade - Kembalikan angka terkecil kedua dalam representasi integer two's complement.
 * Legal ops    : ^ ~ >> <<
 * Max ops      : 4
 * Rating       : 1
 */
int masquerade() {
    return (128 << 24) ^ 1;
}

// Soal 3
/**
 * airani_iofifteen - Kembalikan 1 apabila iofi == 15, dan 0 apabila tidak.
 * kemudian gabungkan dengan bitwise OR.
 * 
 * Contoh:
 * airani_iofifteen(15) = 1
 * airani_iofifteen(-15) = 0
 * airani_iofifteen(69420) = 0
 * 
 * Legal ops    : >> & !
 * Max ops      : 15
 * Rating       : 1
 */
int airani_iofifteen(int iofi) {
    int masked = iofi & 15;
    int digit3 = (masked >> 3) & 1;
    int digit2 = (masked >> 2) & 1;
    int digit1 = (masked >> 1) & 1;
    int digit0 = masked & 1;
    return !(iofi >> 4) & digit0 & digit1 & digit2 & digit3;
}

// Soal 4
/**
 * yobanashi_deceive - Kembalikan sqrt(sqrt(sqrt(f))) dengan pembulatan ke float
 * terdekat ke bawah yang bisa direpresentasikan.
 * 
 * Parameter f adalah sebuah float dalam format 32 bits untuk Exponent 
 * dan 0 bits untuk Mantissa. Kembalikan dalam format yang sama.
 * 
 * Contoh:
 * yobanashi_deceive(0b0) = 0
 * yobanashi_deceive(0b001011) = 0b1
 * yobanashi_deceive(0b10011010001) = 0b10011010
 * 
 * Legal ops    : >>
 * Max ops      : 1
 * Rating       : 2
 */
int yobanashi_deceive(unsigned f) {
    return f >> 3;
}

// Soal 5
/**
 * snow_mix - Kembalikan N + (2 ^ 23).
 * 
 * Ketentuan: dijamin 0 <= N <= (2 ^ 24).
 * Contoh:
 * snow_mix(3) = 8388611
 * snow_mix(31) = 8388639
 * snow_mix(8650816) = 17039424
 * 
 * Legal ops    : ^ >> & << | ~ !
 * Max ops      : 14
 * Rating       : 2
 */
int snow_mix(int N) {
    int x = 1 << 23;
    return ((N&x)<<1)^(N^x);
}

// Soal 6
/**
 * sky_hundred - Kembalikan hasil XOR dari 1 ke n.
 * 
 * Jika n bernilai negatif, kembalikan 0.
 * 
 * Contoh:
 * sky_hundred(33) = 1
 * sky_hundred(20) = 20
 * sky_hundred(-1) = 0
 * 
 * Legal ops    : + ^ >> & << | ~ !
 * Max ops      : 30
 * Rating       : 2
 */
int sky_hundred(int n) {
    int rem = n & 3;
    int neg = ~(n >> 31);
    int mod0 = n & (~(!rem) + 1) & neg;
    int mod1 = 1 & (~(!(rem ^ 1)) + 1) & neg;
    int mod2 = (n + 1) & (~(!(rem ^ 2)) + 1) & neg;
    return (mod0 + mod1 + mod2);
}

// Soal 7
/**
 * ganganji - Mengalikan x dengan 1.125 (bulatkan ke bawah) dengan ketentuan:
 * - Nilai x tidak negatif (tetapi bisa 0).
 * - Jika terjadi overflow, kembalikan 0x7fffffff.
 * 
 * 
 * Contoh:
 * ganganji(7) = 7
 * ganganji(8) = 9
 * ganganji(101) = 113
 * ganganji(2000000000) = 2147483647
 * 
 * Legal ops    : + - ^ >> & << | ~ !
 * Max ops      : 30
 * Rating       : 3
 */
int ganganji(int x) {
    int res = x + (x >> 3);
    int overflow = (res >> 31) ^ (x >> 31);
    int nmax = ~(1 << 31);
    res = ~(overflow) & res;
    return (res + (overflow & nmax));
}

// Soal 8
/**
 * kitsch - Kembalikan x dikalikan dengan 17/64. Bulatkan menuju 0.
 * 
 * Contoh:
 * kitsch(400) = 106
 * kitsch(15) = 3
 * kitsch(-6) = -1
 * kitsch(-10) = -2
 * 
 * Legal ops    : ~ & | << >> ! +
 * Max ops      : 18
 * Rating       : 3
 */
int kitsch(int x) {
    int xper64 = x >> 6; // floor(x/64)
    int rem64 = x & 63; // x % 64
    // Kali 17
    xper64 += xper64 << 4;
    rem64 += rem64 << 4;
    // +1 kalo negatif
    rem64 += (x >> 31 & 63);
    // hasil
    xper64 += rem64 >> 6;
    return xper64;
}

// Soal 9
/**
 * how_to_sekai_seifuku - Kembalikan bit-level equivalent dari ekspresi (int) f.
 * 
 * Argumen f merupakan representasi bit dari bilangan desimal dalam bentuk single-precision floating point.
 * Jika nilai float melebihi batasan (termasuk NaN dan infinity), kembalikan 0x80000000u.
 * 
 * Contoh:
 * how_to_sekai_seifuku(0xFF00) = -inf
 * how_to_sekai_seifuku(0x80c3) = -0.00001162290573
 * how_to_sekai_seifuku(0x0000) = 0.0
 * how_to_sekai_seifuku(0x0001) = 0.000000059604645
 * how_to_sekai_seifuku(0x5B37) = 230.875
 * how_to_sekai_seifuku(0x7F10) = NaN
 * 
 * Contoh 2 dan contoh 4 untuk denormalized, contoh 5 untuk normalized, contoh 6 untuk NaN.
 * 
 * Legal ops    : Konstanta Besar, Conditional, Looping, == >> << - + | & ^
 * Max ops      : 30
 * Rating       : 4
 */
unsigned how_to_sekai_seifuku(unsigned f) {
    unsigned sign = (f >> 15) & 1;
    unsigned exp = (f >> 10) & 31; // masking 5 bit exp dengan & 11111
    unsigned mantissa = f & 1023; // masking 10 bit mantissa dengan 1111111111
    unsigned res = sign << 31;
    // NaN dan +- Inf
    if (exp == 31) {
        if ((mantissa & 1023) == 0) return res | 0x7F800000; // +- inf
        else return 0x7F800001; // NaN
    }
    if (exp == 0) {
        if (mantissa == 0) return res; // Nol bertanda
        while ((mantissa & (1 << 10)) == 0) { // Selagi belum mencapai MSB dari mantissa
            exp -= 1;
            mantissa <<=  1;
        }
        exp += 1;
        mantissa &= 1023;
    }
    exp += 112; // Ubah bias (128 untuk single precision, 15 untuk half precision -> 127 -15)
    return res | (exp << 23) | (mantissa << 13);
}

// Soal 10
/**
 * mesmerizer - Kembalikan bit-level equivalent dari ekspresi (int) f.
 * 
 * Argumen f merupakan representasi bit dari bilangan desimal dalam bentuk single-precision floating point.
 * Jika nilai float melebihi batasan (termasuk NaN dan infinity), kembalikan 0x80000000u.
 * 
 * Contoh:
 * mesmerizer(32.0) = 32
 * mesmerizer(-420.69) = 420
 * mesmerizer(0.000026) = 0
 * mesmerizer(88888888888) = max int
 * 
 * Legal ops    : Konstanta Besar, Conditional, Looping, Tipe Unsigned, all integer operations
 * Max ops      : 30
 * Rating       : 4
 */
int mesmerizer(unsigned uf) {
    unsigned max_int = 1 << 31;
    unsigned sign = uf >> 31;
    unsigned exp = ((uf >> 23) & 255);
    unsigned frac = uf & ((1 << 23) - 1);
    if (exp == 0) return 0; // 0.sesuatu * 2^-126, terlalu kecil
    if (exp == 255) return max_int; // kasus inf, -inf, atau NaN
    exp = exp - 127; // mengurangi dengan bias
    if (exp >> 31 & 1) return 0; // pecahan
    if (!(((exp - 30) >> 31) & 1)) return max_int; // 
    int x = 1 << exp; 
    if (((exp - 23) >> 31) & 1) {
        x |= frac >> (23 - exp);
    } else {
        x |= frac << (exp - 23);
    }
    if (sign == 1) x = ~x + 1;
    return x;
}

// DRIVER UNTUK PENGUJIAN


// int main() {
//     // int n;
//     unsigned n;
//     // "%d" untuk integer, "%u" untuk unsigned, "%x" untuk bentuk heksadesimal
//     scanf("%x", &n);
//     printf("%", how_to_sekai_seifuku(n));
//     return 0;
// }
