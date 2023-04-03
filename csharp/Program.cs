class Program {
  static void Main(string[] args) {
    Console.WriteLine("If you see this text, program run successfully!");
    string name = Ask();
    Console.WriteLine($"Hello, {name}!");
    string Ask() {
      Console.WriteLine("So, what's your name?");
      string res = Console.ReadLine() ?? "null (good name tho)";
      return (res == "" || res == " ") ? Ask() : res;
    }
  }
}