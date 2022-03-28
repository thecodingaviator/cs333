// Test code. There should be exactly one line of code uncommented at a time.
// A line of code must have just one Statement on it. Fortunately, a Block statement is a single Statement,
// so we have a trick for including multiple statements.

// Test Assignment
//a = 2+3-4;
// b = 2+3+4+9*0;

// Test Block
// {a = 5; b = 6; c = a - b;}
// {a = 1; b = 1; c = a < 5 || b < 5 || 6 > 2 && 4 == 5;}

// Test Conditional
//{a = 5; b = 3; if (a > 10 || b < 20 && b > 1) {c = 10;} else {c = 0;}}
//{a = 5; b = 3; if (a > 0 || b < 20 && b > 1) {c = 10;} else {c = 0;}}

// Test For loop
// for (i = 0; i < 5; i = i + 1;) { a = 2 + i; }
//{a = 0; for (i=0; i < 5; i = i + 1;) { a = a+2; }}

// Test While loop
{ a = 5; while (a < 8) { a = a + 1; } }