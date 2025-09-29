import { z } from 'zod'

export interface CustomRagRequest {
  question: string
}

export const CUSTOM_RAG_RESPONSE_SCHEMA = z.object({
  answer: z.string().optional(),
})

export type CustomRagResponse = z.infer<typeof CUSTOM_RAG_RESPONSE_SCHEMA>
