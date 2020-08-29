// Example program
#include <iostream>
#include <string>
#include <map>

using namespace std;

class Item;
void Output_Crafting_Table();

class Item
{
    public:
        string name;
        int worth, damage, amount;
        Item *RECIPE; 
        void Set_Values(string, int, int, int, Item[3][3]);
    
    Item() {}
    Item(string n, int w, int d, int a, Item R[3][3])
    {
        name = n;
        worth = w;
        damage = d;
        amount = a;
        RECIPE = *R;
    }
};

void Item::Set_Values(string n, int w, int d, int a, Item R[3][3])
{
    name = n;
    worth = w;
    damage = d;
    amount = a;
    RECIPE = *R;
}

Item empty = {"Empty", 0,0,0, 0};

Item EMPTY_TABLE [3][3] = 
{
    {empty, empty, empty},
    {empty, empty, empty},
    {empty, empty, empty}
};

Item stick = {"Stick", 2, 3, 1, 0};
Item cobblestone = {"Cobblestone", 1, 0, 1, 0};
Item wood = {"Wood", 5, 0, 1, 0};


Item stone_pick_recipe[3][3] = 
{
    {cobblestone, cobblestone, cobblestone},
    {empty, stick, empty},
    {empty, stick, empty}
};

Item stone_pick = {"Stone Pickaxe", 10, 5, 1, stone_pick_recipe}; // Stone Pickaxe. Consists of 2 sticks and 3 Cobblestone
// enum items {stick = "Stick", cobblestone = "Cobblestone", wood = "Wood"};

map<string, Item> M_Item_Names = 
{ 
    {"stick", stick},
    {"cobblestone", cobblestone},
    {"wood", wood},
    {"stone_pick", stone_pick},
    {"empty", empty}
};



Item CRAFTING_TABLE [3][3] = EMPTY_TABLE;



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
    Output_Crafting_Table();
    cout << "\n";
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
  U_Input();
  U_Input();
  if (CRAFTING_TABLE == stone_pick_recipe)
    {
        cout << "Crafted a Stone Pickaxe!";  
    }
  //U_Input();
  return 0;
}
