function dots(f)
alpha0=pi/6;
K=18;
R=sqrt(3)/2;
[XMesh,YMesh]=meshgrid(1:K);
tList=linspace(0,2*pi,100);
tCos=[cos(tList).*R,nan]';
tSin=[sin(tList).*R,nan]';
tX=tCos+XMesh(:)';tX=tX(:);
tY=tSin+YMesh(:)';tY=tY(:);
figure('Units','normalized','Position',[.3,.2,.5,.65]);
plot(tX,tY,'Color',[0.2,0.2,0.2,.8],'LineWidth',1)
% -----------------------------
ax=gca;hold on;
ax.XLim=[0,K+1];
ax.YLim=[0,K+1];
ax.XColor='none';
ax.YColor='none';
ax.PlotBoxAspectRatio=[1,1,1];
ax.Position=[0,0,1,1];
% -----------------------------
dTheta=2*pi/48;
alpha=flipud(XMesh+YMesh);
thetaMesh=alpha(:).*alpha0;
% -----------------------------
for i=1:f
    thetaMesh=thetaMesh+dTheta;
    pntHdl.XData=cos(thetaMesh).*R+XMesh(:);
    pntHdl.YData=sin(thetaMesh).*R+YMesh(:);
end
%-----------------------------
pntHdl=scatter(cos(thetaMesh).*R+XMesh(:),...
    sin(thetaMesh).*R+YMesh(:),...
    15,sin(thetaMesh).*R,'filled');
set(gca,'Color','k');
set(gcf,'Color','k');
end