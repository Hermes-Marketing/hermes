# Build stage
FROM node:16.16.0 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Development stage
FROM node:16.16.0 as development
WORKDIR /app
COPY --from=build /app .
EXPOSE 8080
CMD ["npm", "run", "dev"]