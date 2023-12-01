import { getParsedData } from "../common/index.ts";

const wordMap = {
  one: "1",
  two: "2",
  three: "3",
  four: "4",
  five: "5",
  six: "6",
  seven: "7",
  eight: "8",
  nine: "9",
};

const sumFirstAndLastDigits = (calibration: string): number => {
  // find first occurance of a digit in the string
  const digits = calibration.match(
    /\d|one|two|three|four|five|six|seven|eight|nine/g
  );

  if (!digits) return 0;

  let firstDigit = digits[0];
  if (isNaN(parseInt(firstDigit))) {
    firstDigit = wordMap[firstDigit as keyof typeof wordMap];
  }

  // convert last match to number, if needed
  let lastDigit = digits[digits.length - 1];
  if (isNaN(parseInt(lastDigit))) {
    lastDigit = wordMap[lastDigit as keyof typeof wordMap];
  }

  return parseInt(firstDigit + lastDigit);
};

const part2 = async (): Promise<number> => {
  const data = await getParsedData(1);
  const nums = data.map((x) => sumFirstAndLastDigits(x));
  return nums.reduce((a, b) => a + b);
};

console.log(await part2());
