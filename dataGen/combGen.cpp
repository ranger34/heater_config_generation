/***************
feature vector:
{P0, (l0,h0), P1, (l1,h1), P2, (l2,h2), P3, (l3,h3), P4, (l4,h4)}
P: (-80, +80), interval 20
temperature configuration: +-2 as the fluctuation
***************/

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
using namespace std;

int main()
{
	//string str_start = "/*modify here*/";
	//string str_end = "/*end modify*/";
	const int N = 28125;
	//string power[9] = { "-80", "-60", "-40", "-20", "0", "20", "40", "60", "80" };
	
	string power[9][5] = {	
		{ "550, 750", "530, 730", "570, 770", "560, 760", "540, 740" },
		{ "570, 770", "550, 750", "590, 790", "580, 780", "560, 760" },
		{ "590, 790", "570, 770", "610, 810", "600, 800", "580, 780" },
		{ "610, 810", "590, 790", "630, 830", "620, 820", "600, 800" },
		{ "630, 830", "610, 810", "650, 850", "640, 840", "620, 820" },	// original
		{ "650, 850", "630, 830", "670, 870", "660, 860", "640, 840" },
		{ "670, 870", "650, 850", "690, 890", "680, 880", "660, 860" },
		{ "690, 890", "670, 870", "710, 910", "700, 900", "680, 880" },
		{ "710, 910", "690, 890", "730, 930", "720, 920", "700, 900" }	
	};
	
	//string config[5] = { "(-2, -2)", "(0, 0)", "(2, 2)", "(-2, 2)", "(2, -2)" };
	
	string config[5][5] = {	
		{ "286, 298", "284, 296", "288, 300", "287, 299", "285, 297" },
		{ "288, 300", "286, 298", "290, 302", "289, 301", "287, 299" },	// original
		{ "290, 302", "288, 300", "292, 304", "291, 303", "289, 301" },
		{ "286, 302", "284, 300", "288, 304", "287, 303", "285, 301" },
		{ "290, 298", "288, 296", "292, 300", "291, 299", "289, 297" }	
	};
	
	string result[N];

	stringstream num;

	int j = 0, a = 0, b = 0, c = 0, d = 0, e = 0;
	for (int i = 0; i < N; i++)
	{
		result[i].clear();
	
		num.str("");
		num << i;       
		result[i] += num.str();	   result[i] += ": ";	  
		// a line
        		
		result[i] += power[j][0];  result[i] += ", ";
		result[i] += config[a][0]; result[i] += ", ";

		result[i] += power[j][1];  result[i] += ", ";
		result[i] += config[b][1]; result[i] += ", ";

		result[i] += power[j][2];  result[i] += ", ";
		result[i] += config[c][2]; result[i] += ", ";

		result[i] += power[j][3];  result[i] += ", ";
		result[i] += config[d][3]; result[i] += ", ";

		result[i] += power[j][4];  result[i] += ", ";
		result[i] += config[e][4];
		
		/*
		result[i] += power[j];  result[i] += ", ";
		result[i] += config[a]; result[i] += ", ";
		result[i] += config[b]; result[i] += ", ";
		result[i] += config[c]; result[i] += ", ";
		result[i] += config[d]; result[i] += ", ";
		result[i] += config[e];
		*/

		if ((i + 1) % (int)pow(5, 5) == 0) j++;
		if ((i + 1) % (int)pow(5, 4) == 0) { a++; a %= 5; }
		if ((i + 1) % (int)pow(5, 3) == 0) { b++; b %= 5; }
		if ((i + 1) % (int)pow(5, 2) == 0) { c++; c %= 5; }
		if ((i + 1) % 5 == 0) { d++; d %= 5; }
		e++; e %= 5;
	}

	char file1[] = "allComb.txt";
	//char file1[] = "refer.txt";
    char file2[] = "part1.txt";
	char file3[] = "remain.txt";

	ofstream fout1(file1);
	ofstream fout2(file2);
	ofstream fout3(file3);

	// all combination
	if (fout1.is_open())
	{
		for(int i = 0; i < N; i++)
			fout1 << result[i] << endl;
		fout1.close();
	}

	// sample part1
	if (fout2.is_open())
	{
		for(int i = 0; i < N; i++)
		{
			if(i % 375 == 0)
				fout2 << result[i] << endl;
		}
		fout2.close();
	}

	//
	if (fout3.is_open())
	{
		for(int i = 0; i < N; i++)
		{
			if(i % 375 != 0)
				fout3 << result[i] << endl;
		}
		fout3.close();
	}

	cout << "done" << endl;

	return 0;
}
