
class PrimeNumber {
  public static void main(String[] args) {
    int num = 18;

    boolean isPrime = true;
    int i = 2;
    while (i < num) {
      if (num % i == 0) {
        isPrime = false;

      }
      i++;
    }

    if (isPrime) {
      System.out.println("Prime");
    } else {
      System.out.println("not prime");
    }
  }
}