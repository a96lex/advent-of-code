import { deepEqual } from "https://deno.land/x/helmet_mods@1.47.4/deps/std_testing.ts";

import { getParsedData } from "../common/index.ts";

type pipes = "|" | "-" | "L" | "J" | "7" | "F" | ".";

type direction = {
  top: boolean;
  right: boolean;
  bottom: boolean;
  left: boolean;
};

const directions: { [key in pipes]: direction } = {
  "|": { top: true, right: false, bottom: true, left: false },
  "-": { top: false, right: true, bottom: false, left: true },
  L: { top: true, right: true, bottom: false, left: false },
  J: { top: true, right: false, bottom: false, left: true },
  "7": { top: false, right: false, bottom: true, left: true },
  F: { top: false, right: true, bottom: true, left: false },
  ".": { top: false, right: false, bottom: false, left: false },
};

type position = { y: number; x: number };

const findStartPosition = (data: string[]): position => {
  for (let y = 0; y < data.length; y++) {
    for (let x = 0; x < data[0].length; x++) {
      if (data[y][x] === "S") return { y, x };
    }
  }
  return { x: 0, y: 0 };
};

const findStartPipe = (
  data: string[],
  position: {
    x: number;
    y: number;
  }
) => {
  const { x, y } = position;

  // see if neighbours connect to here
  let top = false,
    right = false,
    bottom = false,
    left = false;

  // all this is from the POV of the other piece
  if (x > 0) left = directions[data[y][x - 1] as pipes].right;

  if (x < data[0].length) right = directions[data[y][x + 1] as pipes].left;

  if (y > 0) top = directions[data[y - 1][x] as pipes].bottom;

  if (y < data.length) bottom = directions[data[y + 1][x] as pipes].top;

  return {
    top,
    right,
    bottom,
    left,
  };
};

const getNextPosition = (
  data: string[],
  currentDirection: direction,
  currentPosition: position,
  lastPosition: position
) => {
  if (currentDirection.top) {
    if (currentPosition.y > 0) {
      const proposedPosition = { ...currentPosition };
      proposedPosition.y -= 1;
      if (!deepEqual(proposedPosition, lastPosition)) return proposedPosition;
    }
  }

  if (currentDirection.right) {
    if (currentPosition.x < data[0].length) {
      const proposedPosition = { ...currentPosition };
      proposedPosition.x += 1;
      if (!deepEqual(proposedPosition, lastPosition)) return proposedPosition;
    }
  }

  if (currentDirection.bottom) {
    if (currentPosition.y < data.length) {
      const proposedPosition = { ...currentPosition };
      proposedPosition.y += 1;

      if (!deepEqual(proposedPosition, lastPosition)) return proposedPosition;
    }
  }

  if (currentDirection.left) {
    if (currentPosition.x > 0) {
      const proposedPosition = { ...currentPosition };
      proposedPosition.x -= 1;
      if (!deepEqual(proposedPosition, lastPosition)) return proposedPosition;
    }
  }
  return { x: -1, y: -1 };
};

const main = async (): Promise<number> => {
  const data = await getParsedData(10);
  const startPosition = findStartPosition(data);
  const startDirection = findStartPipe(data, startPosition);

  let currentPosition = getNextPosition(
    data,
    startDirection,
    startPosition,
    startPosition
  );
  let lastPosition = { ...startPosition };

  const loop = new Map();
  loop.set(`${startPosition.x}:${startPosition.y}`, true);
  loop.set(`${currentPosition.x}:${currentPosition.y}`, true);

  while (!deepEqual(currentPosition, startPosition)) {
    const nextPosition = getNextPosition(
      data,
      directions[data[currentPosition.y][currentPosition.x] as pipes],
      currentPosition,
      lastPosition
    );
    lastPosition = { ...currentPosition };
    currentPosition = { ...nextPosition };
    loop.set(`${currentPosition.x}:${currentPosition.y}`, true);
  }

  let tiles = 0;

  // inspired by https://github.com/salt-die/Advent-of-Code/blob/main/2023/day_10.py
  // and https://www.reddit.com/r/adventofcode/comments/18fgddy/2023_day_10_part_2_using_a_rendering_algorithm_to/
  let inside: boolean;
  for (let y = 0; y < data.length; y++) {
    inside = false;
    for (let x = 0; x < data[0].length; x++) {
      const position = { x, y };
      let currentPipe = data[y][x];
      // infer from input manually
      if (currentPipe == "S") currentPipe = "F";
      if (!loop.has(`${position.x}:${position.y}`)) {
        tiles += +inside;
      } else if ("|JL".includes(currentPipe)) {
        inside = !inside;
      }
    }
  }

  return tiles;
};

console.log(await main());
