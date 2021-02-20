#include <iostream>
using namespace std;

string getDayOfTheWeek(int dayNum)
{
    string dayName;

    switch (dayNum)
    {
    case 0:
        dayName = "Sunday";
        break;
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thrusday";
        break;
    case 5:
        dayName = "Friday";
        break;
    case 6:
        dayName = "Saturday";
        break;

    default:
        dayName = "N/A";
        break;
    }

    return dayName;
}

int main()
{

    cout << getDayOfTheWeek(10);
    return 0;
}
