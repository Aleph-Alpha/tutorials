import { type Http, http } from '@aleph-alpha/lib-http'
import type { CustomRagResponse, CustomRagRequest } from '@/@core/models/api/customRag.ts'

export const HTTP_CLIENT = http({ timeout: 60_000 })

export class CustomRagService {
  constructor(readonly httpClient: Http) {}

  async customQa(body: CustomRagRequest): Promise<CustomRagResponse> {
    return (await this.httpClient.post<CustomRagResponse>('qa', { body })).data
  }
}

export const CUSTOM_RAG_SERVICE = new CustomRagService(HTTP_CLIENT)
