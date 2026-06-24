/*
  Warnings:

  - A unique constraint covering the columns `[token_hash]` on the table `password_reset_tokens` will be added. If there are existing duplicate values, this will fail.

*/
-- DropIndex
DROP INDEX "password_reset_tokens_expires_at_idx";

-- CreateIndex
CREATE UNIQUE INDEX "password_reset_tokens_token_hash_key" ON "password_reset_tokens"("token_hash");
