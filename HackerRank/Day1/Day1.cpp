using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    
  // Declare second integer, double, and String variables.
    int usuario_i;
    double usuario_d;
    string usuario_s;

    // Read and save an integer, double, and String to your variables.
    cin >> usuario_i;
    cin >> usuario_d;
    
    cin.ignore();
    getline(cin, usuario_s);

    // Print the sum of both integer variables on a new line.
    cout << i + usuario_i << endl;

    // Print the sum of the double variables on a new line.
    cout << fixed << setprecision(1) << d + usuario_d << endl;

    // Concatenate and print the String variables on a new line
    cout << s + usuario_s << endl;
    return 0;
