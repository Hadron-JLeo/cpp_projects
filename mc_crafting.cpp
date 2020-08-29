// Example program
#include <iostream>
#include <string>
#include <map>

using namespace std;

class Item
{
    public:
        string name;
        int worth, damage, amount;
        void Set_Values(string, int, int, int);
    
    Item() {}
    Item(string n, int w, int d, int a)
    {
        name = n;
        worth = w;
        damage = d;
        amount = a;
        
    }
};


void Item::Set_Values(string n, int w, int d, int a)
{
    name = n;
    worth = w;
    damage = d;
    amount = a;
}

Item empty = {"Empty", 0,0,0};
Item stick = {"Stick", 2, 3, 1};
Item cobblestone = {"Cobblestone", 1, 0, 1};
Item wood = {"Wood", 5, 0, 1};
Item stone_pick = {"Stone Pickaxe", 10, 5, 1}; // Stone Pickaxe. Consists of 2 sticks and 3 Cobblestone
// enum items {stick = "Stick", cobblestone = "Cobblestone", wood = "Wood"};

map<string, Item> M_Item_Names = 
{ 
    {"stick", stick},
    {"cobblestone", cobblestone},
    {"wood", wood},
    {"stone_pick", stone_pick},
    {"empty", empty}
};

Item CRAFTING_TABLE [3][3] = 
{
    {empty, empty, empty},
    {empty, empty, empty},
    {empty, empty, empty}
};



Item INVENTORY [4];

Item Craft(Item item, int x, int y) 
{
    CRAFTING_TABLE [x][y] = item;
    cout << "Putting a " << CRAFTING_TABLE [x][y].name << " into the Crafting Table\n";
    return item;
}

Item Name_Comparator(string name) 
{
    return M_Item_Names.at(name);
}

void U_Input() 
{
    
    string name;
    int x, y;
    cin >> name >> x >> y;
    Craft(Name_Comparator(name), x, y);
    
}
void Init_Crafting_Table()
{
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            CRAFTING_TABLE [i][j] = empty;
}

void Output_Crafting_Table()
{
    
    for (int y = 0; y < 3; y++)
    {
        if (y == 1 || y == 2)
            {cout << "\n";}
        
        for (int x = 0; x < 3; x++)   
        {
            if (CRAFTING_TABLE [x][y].name == empty.name) 
            {
                cout << "X ";
            }
            else
            {
                cout << CRAFTING_TABLE [x][y].name << " ";
            }
        
        }
    }    
    
}

int main()
{
  //cout << "Hello World";
  
  U_Input();
  U_Input();
  U_Input();
  Output_Crafting_Table();
  //U_Input();
  return 0;
}
