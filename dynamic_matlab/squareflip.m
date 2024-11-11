function squareflip(f)
ax=axes('position',[0 0 1 1]);
dx=sin(f*0.15);
map=(turbo);
c=map(f*5,:);
x=[-1+dx 1 1-dx -1]*0.8^((f-1)/5);
y=[-1 -1+dx 1 1-dx]*0.8^((f-1)/5);
patch(x,y,c,'edgecolor','none')
hold on
xlim([-1 1])
ylim([-1 1])
axis equal off
end