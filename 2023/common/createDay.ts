let dayNumber = Deno.args[0];

if (!dayNumber) {
  dayNumber = new Date().getDate().toString();
}

const dayDir = `./day${dayNumber.padStart(2, "0")}`;

try {
  if (Deno.statSync(dayDir).isDirectory) {
    console.log(`dir ${dayDir} already exists`);
    Deno.exit(0);
  }
} catch {
  console.log(`creating dir ${dayDir}`);
}

Deno.mkdirSync(dayDir, { recursive: true });

const templateFilePath = "./common/templates/day.template";

const templateContent = await Deno.readTextFile(templateFilePath);

const substitutedContent = templateContent.replace("CURRENT_DAY", dayNumber);

for (let i = 1; i <= 2; i++) {
  const newFilePath = dayDir + `/part${i}.ts`;
  await Deno.writeTextFile(newFilePath, substitutedContent);
}
