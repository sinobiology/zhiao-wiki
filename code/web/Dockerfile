# ── Stage 1: 构建前端 ──────────────────────────────────────────────────────────
FROM node:22-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --ignore-scripts

COPY . .
RUN npm run build

# ── Stage 2: 生产镜像 ──────────────────────────────────────────────────────────
FROM node:22-alpine

WORKDIR /app

# 只复制生产依赖
COPY package*.json ./
RUN npm ci --omit=dev --ignore-scripts

# 复制构建产物和数据
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/public ./public
COPY server.js ./

# 让 Express 同时托管前端静态文件
ENV NODE_ENV=production
ENV PORT=8080

EXPOSE 8080

CMD ["node", "server.js"]
