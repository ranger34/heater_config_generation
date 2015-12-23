/*
feature vector:
{P, (l0,h0), (l1,h1), (l2,h2), (l3,h3), (l4,h4)}
P: (-80, +80), interval 20
temperature configuration: 1 as the fluctuation
*/

#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	//string begin_str = "/*modify here*/";
	//string end_str = "/*end modify*/";
	const int N = 9 * pow(5, 5);
	string power[9] = { "-80", "-60", "-40", "-20", "0", "20", "40", "60", "80" };
	string config[5] = { "-1, -1", "0, 0", "1, 1", "-1, 1", "1, -1" };
	string result;

	char file[] = "configPerm.txt";
	ofstream fout(file);

	if (fout.is_open())
	{
		int j = 0, a = 0, b = 0, c = 0, d = 0, e = 0;
		for (int i = 0; i < N; i++)
		{
			result.clear();
			result += power[j];	result += ", ";
			result += config[a]; result += ", ";
			result += config[b]; result += ", ";
			result += config[c]; result += ", ";
			result += config[d]; result += ", ";
			result += config[e];

			if ((i + 1) % (int)pow(5, 5) == 0) j++;
			if ((i + 1) % (int)pow(5, 4) == 0){
				a++;
				a %= 5;
			}
			if ((i + 1) % (int)pow(5, 3) == 0){
				b++;
				b %= 5;
			}
			if ((i + 1) % (int)pow(5, 2) == 0){
				c++;
				c %= 5;
			}
			if ((i + 1) % 5 == 0){
				d++;
				d %= 5;
			}

			e++;
			e %= 5;

			fout << result << endl;
		}

		fout.close();
	}

	cout << "done" << endl;

	return 0;
}