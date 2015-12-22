/*
feature vector:
	{P, (l0,h0), (l1,h1), (l2,h2), (l3,h3), (l4,h4)}
	P: (-80, +80), interval 20
	temperature configuration: 1 as the fluctuation 
*/

#include <iostream>
#include <string>
#include<fstream>
using namespace std;


int main()
{
	string begin_str, end_str;
	begin_str = "/*modify here*/";
	end_str = "/*end modify*/";
	


	char file1[] = "corePerm.txt";
	ofstream fout1(file1);

	if (fout1.is_open())
	{
		




		fout1.close();
	}
	cout << ""<< endl;

	return 0;
}