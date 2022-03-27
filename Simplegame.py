
#include<iostream>
using namespace std;
int wintic[8][3] = {{0, 1, 2},
{3, 4, 5},
{6, 7, 8},
{0, 3, 6},
{1, 4, 7},
{2, 5, 8},
{0, 4, 8},
{2, 4, 6}};


bool isCWins(char *board, char c)
{

for (int a=0; a<8; a++)
if (board[wintic[a][0]] == c &&
board[wintic[a][1]] == c &&
board[wintic[a][2]] == c )
return true;
return false;
}
bool isValid(char board[9])
{

int xCount=0, oCount=0;
for (int j=0; j<9; j++)
{
if (board[j]=='X') xCount++;
if (board[j]=='O') oCount++;
}


if (xCount==oCount || xCount==oCount+1)
{

if (isCWins(board, 'O'))
{

if (isCWins(board, 'X'))
return false;


return (xCount == oCount);
}


if (isCWins(board, 'X') && xCount != oCount + 1)
return false;


return true;
}
return false;
}
int main()
{
   char board[9];
   for(int k=0;k<9;k++)
     cin>>board[k];
  (isValid(board))? cout <<"YES":cout << "NO";
return 0;
}
