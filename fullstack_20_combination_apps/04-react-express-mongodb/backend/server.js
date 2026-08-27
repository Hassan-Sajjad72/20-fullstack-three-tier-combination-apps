import express from "express";
    import { MongoClient } from "mongodb";
async function checkDb() { const c=new MongoClient(process.env.MONGO_URI,{serverSelectionTimeoutMS:5000}); await c.connect(); await c.db().command({ping:1}); await c.close(); }
    const app=express();
    app.get("/ready", async (_req,res)=>{try{await checkDb();res.json({status:"ok",database:"mongodb"})}catch{res.status(503).json({status:"error"})}});
    app.get("/api/v1/message", (_req,res)=>res.json({message:"04-react-express-mongodb is working"}));
    app.listen(Number(process.env.PORT||4000), process.env.HOST||"0.0.0.0");
