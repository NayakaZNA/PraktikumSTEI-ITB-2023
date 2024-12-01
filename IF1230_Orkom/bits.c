#include<stdio.h>

// Soal 1
int chicken_or_beef(int chicken, int beef) {
    beef = (beef << 1) & 15;
    chicken = (chicken >> 4) & 15;
    return chicken | beef;
}

// Soal 2
int masquerade() {
    return (128 << 24) ^ 1;
}

// Soal 3
int airani_iofifteen(int iofi) {
    int masked = iofi & 15;
    int digit3 = (masked >> 3) & 1;
    int digit2 = (masked >> 2) & 1;
    int digit1 = (masked >> 1) & 1;
    int digit0 = masked & 1;
    return !(iofi >> 4) & digit0 & digit1 & digit2 & digit3;
}

// Soal 4
int yobanashi_deceive(unsigned f) {
    return f >> 3;
}

// Soal 5

int snow_mix(int N) {
    int x = 1 << 23;
    return ((N&x)<<1)^(N^x);
}

// Soal 6
int sky_hundred(int n) {
    int rem = n & 3;
    int neg = ~(n >> 31);
    int mod0 = n & (~(!rem) + 1) & neg;
    int mod1 = 1 & (~(!(rem ^ 1)) + 1) & neg;
    int mod2 = (n + 1) & (~(!(rem ^ 2)) + 1) & neg;
    return (mod0 + mod1 + mod2);
}

// Soal 7
int ganganji(int x) {
    int res = x + (x >> 3);
    int overflow = (res >> 31) ^ (x >> 31);
    int nmax = ~(1 << 31);
    res = ~(overflow) & res;
    return (res + (overflow & nmax));
}

// Soal 8
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

    // unsigned int sign    = f & (1 << 15); // 32768, 0x8000
    // unsigned int nonsign = f & ((1 << 15) - 1); // 32767, 0x7fff
    // unsigned int exp     = f & (31 << 10); // 11111 << 10, untuk masking exp
    // sign = sign << 16; // Menggeser sign ke bit paling kiri
    // // Normalisasi
    // nonsign = nonsign << 13; // Menggeser supaya mantissa mentok dari bit 23 ke kanan
    // nonsign += (7 << 28); // Menambahkan bit 1 ke digit 29-31 (exp) supaya bisa menyesuaikan kondisi 
    // if (exp == 0) return sign;
    // return sign | nonsign;

// Soal 10
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

int main() {
    unsigned n;
    scanf("%x", &n);
    printf("%d", how_to_sekai_seifuku(n));
    return 0;
}
/*
01111111111111111111111111111111
000000000000000011100000
x =                                     0100000000000000000000000
y =                                     0100001000000000001000000
x&y =                                   0100000000000000000000000
x&y<<1 =                                1000000000000000000000000
x^y =                                   0000001000000000001000000
(x&y<<1)^(x^y) =                        1000001000000000001000000
(x&y<<1)&(x^y) =                        0000000000000000000000000
(x&y<<1)&(x^y)<<1 =                     0000000000000000000000000
((x&y<<1)&(x^y)<<1)^((x&y<<1)^(x^y)) =  1000001000000000001000000

x                                   = 0110
y                                   = 0011
x^y                                 = 0101
x&y                                 = 0010
x&y<<1                              = 0100
(x&y<<1)^(x^y)                      = 0001
(x&y<<1)&(x^y)                      = 0100
(x&y<<1)&(x^y)<<1                   = 1000
((x&y<<1)&(x^y)<<1)^(x&y<<1)^(x^y)  = 1001 


x                   = 0101
y                   = 0011
x^y                 = 0110  targ
x&y                 = 0001
x&y<<1              = 0010  carry1
(x&y<<1)^(x^y)      = 0100  carry2
(x&y<<1)^(x^y)<<1   = 1000  targ
*/