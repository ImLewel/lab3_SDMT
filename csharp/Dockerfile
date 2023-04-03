FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /usr/src/csharp-app

COPY csharp.csproj .
RUN dotnet restore csharp.csproj

COPY . .
RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/runtime:6.0 AS runtime
WORKDIR /usr/src/csharp-app
COPY --from=build /usr/src/csharp-app/out ./

ENTRYPOINT ["dotnet", "csharp.dll"]