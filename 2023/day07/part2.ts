import { getParsedData } from "../common/index.ts";

const CardOrder = [
  "A",
  "K",
  "Q",
  "T",
  "9",
  "8",
  "7",
  "6",
  "5",
  "4",
  "3",
  "2",
  "J",
];

const getHandCounts = (hand: string) => {
  const counts = CardOrder.map(() => 0);
  for (let i = 0; i < hand.length; i++) {
    counts[CardOrder.indexOf(hand[i])] += 1;
  }

  const jokers = counts[counts.length - 1];

  if (jokers) {
    counts[counts.length - 1] = 0;
  }

  counts.sort();
  return [counts[counts.length - 1] + jokers, counts[counts.length - 2]];
};

// save cards into array
// make a ordering function
const compareHands = (hand1: string, hand2: string) => {
  const maxLetters1 = getHandCounts(hand1);
  const maxLetters2 = getHandCounts(hand2);

  if (maxLetters1[0] > maxLetters2[0]) {
    return 1;
  }

  if (maxLetters1[0] < maxLetters2[0]) {
    return -1;
  }

  if (maxLetters1[1] > maxLetters2[1]) {
    return 1;
  }

  if (maxLetters1[1] < maxLetters2[1]) {
    return -1;
  }

  // order
  for (let i = 0; i < 5; i++) {
    if (CardOrder.indexOf(hand1[i]) > CardOrder.indexOf(hand2[i])) {
      return -1;
    }

    if (CardOrder.indexOf(hand1[i]) < CardOrder.indexOf(hand2[i])) {
      return 1;
    }
  }
  return 0;
};

const main = async (): Promise<number> => {
  const data = await getParsedData(7);

  const hands: (string | number)[][] = [];
  data.map((line) => {
    const split = line.split(" ");
    hands.push([split[0], parseInt(split[1])]);
  });

  hands.sort((a, b) => {
    return compareHands(a[0] as string, b[0] as string) as number;
  });

  return hands.reduce(
    (acc, value, idx) => (value[1] as number) * (idx + 1) + acc,
    0
  );
};

console.log(await main());

/*
32T3K
KK677
T55J5
QQQJA
KTJJT
*/
