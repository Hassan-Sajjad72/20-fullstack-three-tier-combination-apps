import { Controller, Get, Res } from "@nestjs/common";
import type { Response } from "express";
import { MongoClient } from "mongodb";
@Controller()
export class AppController {
  private async checkDb() { const c=new MongoClient(process.env.MONGO_URI!,{serverSelectionTimeoutMS:5000});try{await c.connect();await c.db().command({ping:1});}finally{await c.close();} }
  @Get("health")
  async health(@Res() response: Response) {
    try { await this.checkDb(); return response.json({status:"ok",database:"mongodb"}); }
    catch { return response.status(503).json({status:"error"}); }
  }
  @Get("backend/message")
  message() { return {message:"11-react-nestjs-mongodb is working"}; }
}
