library(maps)
library(mapdata)
require(ggplot2)
require(mapproj)
require(shiny)
require(plyr)

load("~/Downloads/mymatrix-2.Rda")
states<-df$location

getStateVec<-function(location){
  states<- str_extract(location,", [A-Z]{2}")
  states <- str_replace(states,", ","")
  short<-read.csv("~/Downloads/State.csv",header=FALSE)
  names(short)<-c("Long","Short")
  short$Long<-as.character(short$Long)
  getState<-function(shortname){
    if(is.na(shortname)) {
      return (NA)}else{
        ind<-which(short$Short==shortname)[1]
        return (as.character(short$Long[ind]))
      }
  }
  sname<-sapply(states,getState)
}

topnames<-c("Python","R","SQL","EXCEL","C","MATLAB","C++","Hive","Spark","Unix","Perl")

getmapdata<-function(d){
  temp<-d[,topnames]
  temp<-colSums(temp)/nrow(temp)
  colnames(temp)<-toolname
  return (temp)
}

df.test1 <- read.csv("/Volumes/Bootcamp/Hackathon/allresult.csv",header=TRUE)
State1<-getStateVec(df.test1$location)
ind<-as.numeric(mymatrix$id)
State1<-State[ind]
my.backup<-mymatrix

df.test2 <- read.csv("/Volumes/Bootcamp/Hackathon/stack/sf_all.csv",header=TRUE)
State2<-getStateVec(df.test2$location)
State_total<-c(State1,State2)
load("~/Downloads/mymatrix-6.Rda")
mymatrix$State <- State_total

topnames<-tolower(c("Python","R","SQL","EXCEL","C","MATLAB","C++","Hive","Spark","Unix","Perl"))
getmapdata<-function(d){
  temp<-d[,topnames]
  temp<-colSums(temp)
  names(temp)<-topnames
  return (temp)
}

df <-ddply(mymatrix,.(State), getmapdata)
num <- ddply(mymatrix,.(State), nrow)
df$total <- num$V1
df<-df[!is.na(df$State),]

save(df,file="job.result.rda")


