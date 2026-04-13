# ── Etapa 1: Build ──────────────────────────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app

# Copiar dependencias y instalar
COPY package.json package-lock.json* ./
RUN npm install

# Copiar el resto del código
COPY . .

# La variable VITE_API_URL se inyecta en build time via ARG/ENV
ARG VITE_API_URL=http://localhost/api
ENV VITE_API_URL=$VITE_API_URL

# Generar el build de producción
RUN npm run build

# ── Etapa 2: Servidor Nginx ──────────────────────────────────────
FROM nginx:alpine

# Copiar el build generado al directorio de Nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Copiar configuración personalizada de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]